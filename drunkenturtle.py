#-----------------------------------------------------------------------
# drunkenturtle.py
#-----------------------------------------------------------------------

import sys
import random
import stddraw
import turtle

#-----------------------------------------------------------------------

# Accept as command-line arguments an integer t specifying a number of 
# iterations, and a float step specifying a step size. Create a Turtle
# object, and have it make random steps of the given step size. Repeat
# t times.

def main(args):
    t = int(args[1])
    step = float(args[2])
    stddraw.createWindow()
    myTurtle = turtle.Turtle(0.5, 0.5, 0.0)
    for t1 in range(t):
        myTurtle.turnLeft(360.0 * random.random())
        myTurtle.goForward(step)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
    
#-----------------------------------------------------------------------

# Example execution:
#
# python drunkenturtle.py 10000 .01
