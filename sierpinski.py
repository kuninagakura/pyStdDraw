#-----------------------------------------------------------------------
# sierpinski.py
#-----------------------------------------------------------------------

import sys
import stddraw
import stdrandom

# Accept integer n as a command-line argument. Play chaos game on
# triangle to produce Sierpinski triangle of n points.

def main(argv):
    n = int(sys.argv[1])

    stddraw.createWindow()
    cx = [0.000, 1.000, 0.500]
    cy = [0.000, 0.000, 0.866]

    x = 0.0
    y = 0.0

    for i in range(n):
        r = stdrandom.uniformInt(0, 3)
        x = (x + cx[r]) / 2.0
        y = (y + cy[r]) / 2.0
        stddraw.setPenRadius(0.001)
        stddraw.point(x, y)

    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
