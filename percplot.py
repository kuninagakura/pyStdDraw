
#-----------------------------------------------------------------------
# percplot.py
#   python percplot.py 20
#   python percplot.py 100
#-----------------------------------------------------------------------

import sys
import stddraw
import estimate

#-----------------------------------------------------------------------

# Perform experiments and plot results.

def curve(n, x0, y0, x1, y1):
    # print 'curve', N, x0, y0, x1, y1
    gap = .01
    err = .0025
    T = 10000
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.eval(n, xm, T)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show()
        return
    curve(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show()

    curve(n, xm, fxm, x1, y1)

#-----------------------------------------------------------------------

def main(argv):
    n = int(argv[1])
    stddraw.createWindow()
    curve(n, 0.0, 0.0, 1.0, 1.0)
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
