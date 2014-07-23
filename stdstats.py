"""
stdstats.py

The stdstats module defines functions related to statistical analysis
and graphical data display.
"""

#-----------------------------------------------------------------------

import math
import stddraw

#-----------------------------------------------------------------------

def min(a):
    """
    Return the minimum value in array 'a'.  Could call the built-in
    min() function instead.
    """
    minumum = float('inf')
    for x in a:
        if x < minumum:
            minumum = x
    return minumum

#-----------------------------------------------------------------------

def max(a):
    """
    Return the maximum value in array 'a'.  Could call the built-in
    max() function instead.
    """
    maximum = float('-inf')
    for x in a:
        if x > maximum:
            maximum = x
    return maximum

#-----------------------------------------------------------------------

def mean(a):
    """
    Return the average of the values in array 'a'.
    Could call the built-in sum() and len() functions instead.
    """
    sum = 0.0
    for x in a:
        sum += x
    return sum / float(len(a))

#-----------------------------------------------------------------------

def var(a):
    """
    Return the sample variance of the values in array 'a'.
    """
    avg = mean(a)
    sum = 0.0
    for x in a:
        sum += (x - avg) * (x - avg)
    return sum / (float(len(a)) - 1.0)

#-----------------------------------------------------------------------

def stddev(a):
    """
    Return the standard deviation of the values in array 'a'.
    """
    return math.sqrt(var(a))

#-----------------------------------------------------------------------

def median(a):
    """
    Return the median of the values in array 'a'.
    """
    b = list(a)  # Make a copy of a.
    b.sort()
    length = len(b)
    if length % 2 == 1:
        return b[length//2]
    else:
        return float(b[length//2 - 1] + b[length//2]) / 2.0

#-----------------------------------------------------------------------

def plotPoints(a):
    """
    Plot the values of array 'a' as points.
    """
    N = len(a)
    stddraw.setXscale(0, N-1)
    stddraw.setPenRadius(1.0 / (3.0 * N))
    for i in range(N):
        stddraw.point(i, a[i])

#-----------------------------------------------------------------------

def plotLines(a):
    """
    Plot the values of array 'a' as line end-points.
    """
    N = len(a)
    stddraw.setXscale(0, N-1)
    stddraw.setPenRadius()
    for i in range(1, N):
        stddraw.line(i-1, a[i-1], i, a[i])

#-----------------------------------------------------------------------

def plotBars(a):
    """
    Plot the values of array 'a' as bars.
    """
    N = len(a)
    stddraw.setXscale(0, N-1)
    for i in range(N):
        stddraw.filledRectangle(i, a[i]/2, .25, a[i])

#-----------------------------------------------------------------------

def main():
    """
    For testing:
    """
    import stdarray
    import stdio

    a = stdarray.readFloat1D()
    stdio.writef('       min %7.3f\n', min(a))
    stdio.writef('      mean %7.3f\n', mean(a))
    stdio.writef('       max %7.3f\n', max(a))
    stdio.writef('   std dev %7.3f\n', stddev(a))
    stdio.writef('    median %7.3f\n', median(a))

if __name__ == '__main__':
    main()
