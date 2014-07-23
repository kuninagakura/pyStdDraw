#-----------------------------------------------------------------------
# functiongraph.py
#-----------------------------------------------------------------------

import stdarray
import stddraw
import sys
import math

# Accept integer command-line argument n. Plot the function
#     y = sin(4x) + sin(20x)
# between x = 0 and x = pi by drawing n line segments.

# Accept the number of line segments to plot.
n = int(sys.argv[1])
stddraw.createWindow()

# The function y = sin(4x) + sin(20x), sampled at n points
# between x = 0 and x = pi.
x = stdarray.create1D(n+1, 0.0)
y = stdarray.create1D(n+1, 0.0)
for i in range(n+1):
    x[i] = math.pi * i / n
    y[i] = math.sin(4.0*x[i]) + math.sin(20.0*x[i])

# Rescale the coordinate system.
stddraw.setXscale(0, math.pi)
stddraw.setYscale(-2.0, +2.0)

# Plot the approximation to the function.
for i in range(n):
    stddraw.line(x[i], y[i], x[i+1], y[i+1])
    
stddraw.show()
stddraw.wait()
