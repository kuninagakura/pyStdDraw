#-----------------------------------------------------------------------
# recursivesquares.py
#-----------------------------------------------------------------------

import stddraw
import sys

#-----------------------------------------------------------------------

# 2.2 ratio looks good.
RATIO = 2.2

#-----------------------------------------------------------------------

# Plot a square, centered on (x, y) whose sides are fo length size,
# with a light gray background and black border

def drawSquare(x, y, size):
    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.filledSquare(x, y, size/2)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.square(x, y, size/2)

#-----------------------------------------------------------------------

# Plot an order n recursive squares pattern
# centered on (x, y) of the given side length

def draw(n, x, y, size):
    if n == 0:
        return

    drawSquare(x, y, size)

    # Recursively draw 4 smaller trees of order n-1.
    draw(n-1, x - size/2, y - size/2, size/RATIO)    # lower left
    draw(n-1, x - size/2, y + size/2, size/RATIO)    # upper left
    draw(n-1, x + size/2, y - size/2, size/RATIO)    # lower right
    draw(n-1, x + size/2, y + size/2, size/RATIO)    # upper right

#-----------------------------------------------------------------------

# Accept integer command-line argument n and plot an order n recursive
# squares pattern.

def main(argv):
    n = int(argv[1])
    
    stddraw.createWindow()
    x = 0.5     # center of square
    y = 0.5     # center of square
    size = 0.5  # side length of square
    draw(n, x, y, size)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
