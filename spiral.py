#-----------------------------------------------------------------------
# spiral.py
#-----------------------------------------------------------------------

import sys
import stddraw
import turtle
import math

#-----------------------------------------------------------------------

# Accept an integer command-line argument specifying a number of 
# steps, and an float command-line argument specifying a decay factor.
# Draw a spiral using those values.

def main(argv):
    n = float(argv[1])
    decay = float(argv[2])
    stddraw.createWindow()
    stddraw.setPenRadius(0)
    angle = 360.0 / n
    step = math.sin(math.radians(angle/2.0))
    t = turtle.Turtle(0.5, 0, angle/2.0)

    i = 0
    while i < 10.0 * 360.0 / angle:
        step /= decay
        t.goForward(step)
        t.turnLeft(angle)
        i += 1
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
    
#-----------------------------------------------------------------------

# Example executions:

# python spiral.py 3 1.0
# python spiral.py 3 1.2
# python spiral.py 1440 1.0004
# python spiral.py 1440 1.00004
