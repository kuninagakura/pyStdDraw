#-----------------------------------------------------------------------
# tree.py
#-----------------------------------------------------------------------

import stddraw
import sys
import math

#-----------------------------------------------------------------------

BEND_ANGLE   = math.radians(15)
BRANCH_ANGLE = math.radians(37)
BRANCH_RATIO = .65

#-----------------------------------------------------------------------

# Draw a fractal tree of order n rooted at (x, y) at angle a having
# branch radius branchRadius.

def tree(n, x, y, a, branchRadius):
    cx = x + math.cos(a) * branchRadius
    cy = y + math.sin(a) * branchRadius
    stddraw.setPenRadius(.001 * (n ** 1.2))
    stddraw.line(x, y, cx, cy)
    stddraw.show()
    if (n == 0):
        return

    tree(n-1, cx, cy, a + BEND_ANGLE - BRANCH_ANGLE, \
        branchRadius * BRANCH_RATIO)
    tree(n-1, cx, cy, a + BEND_ANGLE + BRANCH_ANGLE, \
        branchRadius * BRANCH_RATIO)
    tree(n-1, cx, cy, a + BEND_ANGLE, \
        branchRadius * (1 - BRANCH_RATIO))

#-----------------------------------------------------------------------

# Accept integer command-line argument n. Draw a fractal tree of
# order n.

def main(argv):
    n = int(argv[1])
    stddraw.createWindow()
    tree(n, .5, 0, math.pi/2, .3)
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
