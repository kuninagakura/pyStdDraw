#-----------------------------------------------------------------------
# plotfilter.py
#-----------------------------------------------------------------------

import stdio
import stddraw

# Plot the points read from standard input.

x0 = stdio.readFloat()
y0 = stdio.readFloat()
x1 = stdio.readFloat()
y1 = stdio.readFloat()

stddraw.createWindow()
stddraw.setXscale(x0, x1)
stddraw.setYscale(y0, y1)
stddraw.setPenRadius(0.001)

# Read and plot the points.
while not stdio.isEmpty():
    x = stdio.readFloat()
    y = stdio.readFloat()
    stddraw.point(x, y)

stddraw.show()
stddraw.wait()
