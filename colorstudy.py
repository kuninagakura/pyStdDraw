#-----------------------------------------------------------------------
# colorstudy.py
#-----------------------------------------------------------------------

import stddraw
import color

# Display Albers squares for all 256 blues and grays.

def main():
    stddraw.createWindow()
    stddraw.setXscale(0, 15)
    stddraw.setYscale(0, 15)
    for i in range(16):
        for j in range (16):
            #val = i + 16*j
            val = 8*i + 8*j
            #c1 = color.Color(0, 0, 255-val)
            c1 = color.Color(255-val, 255-val, 255)            
            c2 = color.Color(val, val, val)
            stddraw.setPenColor(c1)
            stddraw.filledSquare(i, j, 0.5)
            stddraw.setPenColor(c2)
            stddraw.filledSquare(i, j, 0.25)
            stddraw.show()
    stddraw.wait()
    
if __name__ == '__main__':
    main()
