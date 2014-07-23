
#-----------------------------------------------------------------------
# visualize.py
#   python visualize.py 20 .65 1
#   python visualize.py 20 .60 1
#   python visualize.py 20 .55 1
#-----------------------------------------------------------------------

import sys
import stddraw
import percolation

#-----------------------------------------------------------------------

def main(argv):
    n = int(argv[1])
    p = float(argv[2])
    t = int(argv[3])
    stddraw.createWindow()
    for i in range(t):
        open = percolation.random(n, p)
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        percolation.show(open, False)
        stddraw.setPenColor(stddraw.BLUE)
        full = percolation.flow(open)
        percolation.show(full, True)
        stddraw.sleep(1000)
        stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
