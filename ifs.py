#-----------------------------------------------------------------------
# ifs.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stdrandom
import stddrawtkinter as stddraw

#-----------------------------------------------------------------------

# Accept integer t as a command-line argument. Read IFS data from
# standard input. Plot t iterations on stddraw.

def main(argv):
    t = int(argv[1])
    dist = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()
    x = 0.0
    y = 0.0
    #stddraw.createWindow()
    for t1 in range(t):
        r = stdrandom.discrete(dist)
        x0 = cx[r][0]*x + cx[r][1]*y + cx[r][2]
        y0 = cy[r][0]*x + cy[r][1]*y + cy[r][2]
        x = x0
        y = y0
        stddraw.setPenRadius(0.001)
        stddraw.point(x, y)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
    
#-----------------------------------------------------------------------

# Example executions:
#
#   python ifs.py 10000 < sierpinski.txt
#   python ifs.py 10000 < barnsley.txt
#   python ifs.py 10000 < binary.txt
#   python ifs.py 10000 < coral.txt
#   python ifs.py 10000 < culcita.txt
#   python ifs.py 10000 < cyclosorus.txt
#   python ifs.py 10000 < dragon.txt
#   python ifs.py 10000 < fishbone.txt
#   python ifs.py 10000 < floor.txt
#   python ifs.py 10000 < koch.txt
#   python ifs.py 10000 < spiral.txt
#   python ifs.py 10000 < swirl.txt
#   python ifs.py 10000 < tree.txt
#   python ifs.py 10000 < zigzag.txt
