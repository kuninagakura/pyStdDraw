#-----------------------------------------------------------------------
# brownian.py
#   python brownian.py 1
#   python brownian.py .5
#   python brownian.py .05
#-----------------------------------------------------------------------

import sys
import math
import stddraw
import stdrandom

#-----------------------------------------------------------------------

def curve(x0, y0, x1, y1, var, s):
    if (x1 - x0) < .01:
        stddraw.line(x0, y0, x1, y1)
        return
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    delta = stdrandom.gaussian(0, math.sqrt(var))
    curve(x0, y0, xm, ym+delta, var/s, s)
    curve(xm, ym+delta, x1, y1, var/s, s)

#-----------------------------------------------------------------------

def main(argv):
    H = float(argv[1])
    stddraw.createWindow()
    s = 2 ** (2*H)  # or this: s = math.pow(2, 2*H)
    curve(0, .5, 1.0, .5, .01, s)
    
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
