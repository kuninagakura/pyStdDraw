#-----------------------------------------------------------------------
# percolation.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Fill every site reachable from the top row.

def flow(open):
    n = len(open)
    full = stdarray.create2D(n, n, False)
    # Percolation flow computation goes here.
    for j in range(n):
        flowHelp(open, full, 0, j)
    return full

#-----------------------------------------------------------------------

# Fill every site reachable from (i, j).

def flowHelp(open, full, i, j):
    n = len(full)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if not open[i][j]:
        return
    if full[i][j]:
        return
    full[i][j] = True
    flowHelp(open, full, i+1, j  )  # Down.
    flowHelp(open, full, i  , j+1)  # Right.
    flowHelp(open, full, i  , j-1)  # Left.
    flowHelp(open, full, i-1, j  )  # Up.

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

# Example executions:

# python percolation.py < test5.txt
# python percolation.py < test8.txt
