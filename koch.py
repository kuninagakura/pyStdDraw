#-----------------------------------------------------------------------
# koch.py
#-----------------------------------------------------------------------

import stddraw
import turtle

# Plot to stddraw a  Koch curve of order n, with given step size,
# using Turtle object tur.

def koch(n, step, tur):
    if n == 0:
        tur.goForward(step)
        return  
    koch(n-1, step, tur)
    tur.turnLeft(60.0)
    koch(n-1, step, tur)
    tur.turnLeft(-120.0)
    koch(n-1, step, tur)
    tur.turnLeft(60.0)
    koch(n-1, step, tur)
 
# Accept integer n as a command-line argument. Plot a Koch curve of 
# order n to stddraw.

def main(argv):
    n = int(argv[1])
    stddraw.createWindow()
    step = 1.0 / (3.0 ** n)
    tur = turtle.Turtle(0.0, 0.0, 0.0)
    koch(n, step, tur)
    stddraw.show()
    stddraw.wait()
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
