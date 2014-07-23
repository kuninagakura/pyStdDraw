#-----------------------------------------------------------------------
# randomsurferhistogram.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import stddraw
import sys
import random

t = int(sys.argv[1])   # number of moves
n = stdio.readInt()    # number of pages
stdio.readInt()        # ignore integer required by input format

# Read transition matrix.
# p[i][j] = prob. that surfer moves from page i to page j
p = stdarray.create2D(n, n, 0.0)
for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()

# freq[i] = # times surfer hits page i
freq = stdarray.create1D(n, 0)

# Start at page 0.
page = 0
stddraw.createWindow()
stddraw.setXscale(-1, n)
stddraw.setYscale(0, t)
#stddraw.setPenRadius(.5/float(n))
stddraw.setPenRadius()
for i in range(t):

    # Make one random move.
    r = random.random()
    sum = 0.0;
    for j in range(n):
        # Find interval containing r.
        sum += p[page][j]
        if r < sum:
            page = j
            break
    freq[page] += 1

    if i % 1000 == 0:
        # Plot histogram of frequencies
        stddraw.clear();
        for k in range(n):
            stddraw.line(k, 0, k, freq[k])
        stddraw.show()

# Print page ranks.
for i in range(n):
    stdio.writef("%8.5f", float(freq[i]) / float(t))
stdio.writeln()

stddraw.wait()

#-----------------------------------------------------------------------
# Example executions:
#
# python transition.py < tiny.txt | python randomsurferhistogram.py 1000000
# python transition.py < medium.txt | python randomsurferhistogram.py 1000000
