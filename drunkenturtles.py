#-----------------------------------------------------------------------
# drunkenturtles.py
#-----------------------------------------------------------------------

import sys
import random
import stddraw
import turtle

# Accept as command-line arguments an integer n specifying a number of
# turtles, an integer t specifying a number of iterations, and a float
# step specifying a step size. Create n Turtle objects, and have them
# make random steps of the given step size. Repeat t times.


def main(args):
    n = int(args[1])
    t = int(args[2])
    step = float(args[3])
    stddraw.createWindow()
    turtles = []
    for i in range(n):
        turtles += \
            [turtle.Turtle(random.random(), random.random(), 0.0)]
    for t1 in range(t):
        for i in range(n):
            turtles[i].turnLeft(360.0 * random.random())
            turtles[i].goForward(step)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
    
#-----------------------------------------------------------------------

# Example executions:
#
# python drunkenturtles.py 20 500 .005
# python drunkenturtles.py 20 1000 .005
# python drunkenturtles.py 20 5000 .005
