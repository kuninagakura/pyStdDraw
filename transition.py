#-----------------------------------------------------------------------
# transition.py
#-----------------------------------------------------------------------

import stdio
import stdarray

# Read links from standard input and write the corresponding
# transition matrix to standard output. First, process the input
# to count the outlinks from each page. Then apply the 90-10 rule to
# compute the transition matrix. Assume that there are no pages that
# have no outlinks in the input.

n = stdio.readInt()

counts = stdarray.create2D(n, n, 0)
outDegree = stdarray.create1D(n, 0)

while not stdio.isEmpty():
    # Accumulate link counts.
    i = stdio.readInt()
    j = stdio.readInt()
    outDegree[i] += 1
    counts[i][j] += 1

stdio.writeln(str(n) + ' ' + str(n))

for i in range(n):
    # Print probability distribution for row i.
    for j in range(n):
        # Print probability for column j.
        p = .90 * float(counts[i][j])/float(outDegree[i]) + .10/float(n)
        stdio.writef('%5.2f', p)
    stdio.writeln()

#-----------------------------------------------------------------------
# Example executions:
#
#    transition.py < tiny.txt
#    transition.py < medium.txt
