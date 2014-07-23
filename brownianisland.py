#-----------------------------------------------------------------------
# brownianisland.py
#-----------------------------------------------------------------------

import stddraw
import stdrandom
import sys
import math

#-----------------------------------------------------------------------

def midpoint(x0, y0, x1, y1, var, n):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        stddraw.show()
        return
    xmid = 0.5 * (x0 + x1) + stdrandom.gaussian(0, math.sqrt(var))
    ymid = 0.5 * (y0 + y1) + stdrandom.gaussian(0, math.sqrt(var))

    midpoint(x0, y0, xmid, ymid, var / 2.7, n-1)
    midpoint(xmid, ymid, x1, y1, var / 2.7, n-1)

#-----------------------------------------------------------------------

# Accept float command-line argument var and integer command-line
# argument n. Plot a Brownian island using var and n with the midpoint
# displacement method.

def main(argv):
    var = float(argv[1])
    n = int(argv[2])
    stddraw.createWindow()
    stddraw.clear()
    stddraw.setXscale(-1, +1)
    stddraw.setYscale(-1, +1)
    midpoint(0, 0, 0, 0, var / math.sqrt(2), n)
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)

#-----------------------------------------------------------------------

# Example execution:

# python brownianisland.py 0.5 11

