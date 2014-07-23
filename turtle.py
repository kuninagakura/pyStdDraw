#-----------------------------------------------------------------------
# turtle.py
#-----------------------------------------------------------------------

import stddraw
import math

#-----------------------------------------------------------------------

class Turtle:

    # Construct a new Turtle object at (x, y) facing a degrees
    # counterclockwise from the x-axis.
    def __init__(self, x, y, a):
        self._x = x      # x value of position in unit square
        self._y = y      # y value of position in unit square
        self._angle = a  # direction of motion (degrees,
                         # counterclockwise from x-axis)

    # Rotate Turtle object self counterclockwise delta degrees.
    def turnLeft(self, delta):
        self._angle += delta

    # Move Turtle object self forward. The distance traversed is
    # defined by step. Draw a line while moving.
    def goForward(self, step):
        oldx = self._x
        oldy = self._y
        self._x += step * math.cos(math.radians(self._angle))
        self._y += step * math.sin(math.radians(self._angle))
        stddraw.line(oldx, oldy, self._x, self._y)

#-----------------------------------------------------------------------

# Accept integer n from the command-line. Draw an n-gon to stddraw.

def main(argv):
    n = int(argv[1])
    stddraw.createWindow()
    turtle = Turtle(.5, .0, 180.0/n)
    for i in range(n):
        step = math.sin(math.radians(180.0/n))
        turtle.goForward(step)
        turtle.turnLeft(360.0/n)
    stddraw.wait()

if __name__ == '__main__':
    import sys
    main(sys.argv)

#-----------------------------------------------------------------------

# Example executions:

# python turtle.py 3
# python turtle.py 7
# python turtle.py 30
