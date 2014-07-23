#-----------------------------------------------------------------------
# histogram.py
#-----------------------------------------------------------------------

import stddraw
import stdstats
import stdarray

#-----------------------------------------------------------------------

class Histogram:

    # Construct a new Histogram object capable of storing n frequency
    # counts.
    def __init__(self, n):
        self._freq = stdarray.create1D(n, 0.0)  # Frequency counts.
        self._max = 0.0                         # Maximum frequency.

    # Add one occurrence of the value i to Histogram object self.
    def addDataPoint(self, i):
        self._freq[i] += 1
        if self._freq[i] > self._max:
            self._max = self._freq[i]
        #self.draw()

    # Draw Histogram object self.
    def draw(self):
        stddraw.setYscale(0, self._max)
        stdstats.plotBars(self._freq)

#-----------------------------------------------------------------------

def main(argv):

    import bernoulli

    coinCount = int(argv[1])
    trialCount = int(argv[2])
    histogram = Histogram(coinCount + 1)
    for trial in range(trialCount):
        histogram.addDataPoint(bernoulli.binomial(coinCount))
  
    stddraw.createWindow(500, 100)
    histogram.draw()
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    import sys
    main(sys.argv)

#-----------------------------------------------------------------------

# Example execution:

# python histogram.py 50 1000000
