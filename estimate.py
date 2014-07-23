
#-----------------------------------------------------------------------
# estimate.py
#   python estimate.py 20 .5 10
#   python estimate.py 20 .75 10
#   python estimate.py 20 .95 10
#   python estimate.py 20 .85 10
#   python estimate.py 20 .85 1000
#   python estimate.py 20 .85 1000
#   python estimate.py 20 .85 100
#-----------------------------------------------------------------------

import sys
import stdio
import percolation

#-----------------------------------------------------------------------

# Generate t random networks, return empirical
# percolation probability estimate.

def eval(n, p, t):
    cnt = 0
    for i in range(t):
        # Generate one random network.
        open = percolation.random(n, p)
        if (percolation.percolates(open)):
            cnt += 1
    return float(cnt) / t

#-----------------------------------------------------------------------

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    t = int(sys.argv[3])
    q = eval(n, p, t)
    stdio.writeln(q)

if __name__ == '__main__':
    main()
