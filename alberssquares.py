#-----------------------------------------------------------------------
# alberssquares.py
#-----------------------------------------------------------------------

import sys
import stddraw
import color

#-----------------------------------------------------------------------

# Accept integers r1, g1, b1, r2, g2, and b2 as command-line arguments.
# Draw Albers squares using colors (r1, g1, b1) and (r2, g2, b2).

def main(argv):
    r1 = int(argv[1])
    g1 = int(argv[2])
    b1 = int(argv[3])

    c1 = color.Color(r1, g1, b1)

    r2 = int(argv[4])
    g2 = int(argv[5])
    b2 = int(argv[6])

    c2 = color.Color(r2, g2, b2)
    stddraw.createWindow()
    stddraw.setPenColor(c1)
    stddraw.filledSquare(.25, .5, .2)

    stddraw.setPenColor(c2)
    stddraw.filledSquare(.25, .5, .1)

    stddraw.setPenColor(c2)
    stddraw.filledSquare(.75, .5, .2)

    stddraw.setPenColor(c1)
    stddraw.filledSquare(.75, .5, .1)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
    
#-----------------------------------------------------------------------

# Example execution:
#    
# python alberssquares.py 0 174 239 147 149 252
