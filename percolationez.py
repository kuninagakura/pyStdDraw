#-----------------------------------------------------------------------
# percolationez.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------

def flow(open):
    n = len(open)
    full = stdarray.create2D(n, n, False)
    # Percolation flow computation goes here.
    for j in range(n):
        full[0][j] = open[0][j]
    for i in range(1, n):
        for j in range(n):
            full[i][j] = open[i][j] and full[i-1][j]
    return full

#-----------------------------------------------------------------------

def percolates(open):
    full = flow(open)
    n = len(full)
    for j in range(n):
        if full[n-1][j]:
            return True
    return False

#-----------------------------------------------------------------------

def show(a, which):
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setYscale(-1, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n-i-1, .5)
                stddraw.show()
#-----------------------------------------------------------------------

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

#-----------------------------------------------------------------------

def main():
    open = stdarray.readBoolean2D()
    stdarray.write2D(flow(open))
    stdio.writeln(percolates(open))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# Example execuxtion:

# python percolationez.py < testez.txt
