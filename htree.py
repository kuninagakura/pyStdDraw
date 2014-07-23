
#-----------------------------------------------------------------------
# htree.py
#   python htree.py 3
#   python htree.py 4
#   python htree.py 5
#-----------------------------------------------------------------------

import stddraw
import sys

#-----------------------------------------------------------------------

def draw(n, sz, x, y):
    if n == 0:
        return
    x0 = x - sz/2
    x1 = x + sz/2
    y0 = y - sz/2
    y1 = y + sz/2

    stddraw.line(x0, y, x1, y)
    stddraw.line(x0, y0, x0, y1)
    stddraw.line(x1, y0, x1, y1)
    stddraw.show()

    draw(n-1, sz/2, x0, y0)
    draw(n-1, sz/2, x0, y1)
    draw(n-1, sz/2, x1, y0)
    draw(n-1, sz/2, x1, y1)

#-----------------------------------------------------------------------

def main(argv):
    n = int(argv[1])
    stddraw.createWindow()
    draw(n, .5, .5, .5)
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
