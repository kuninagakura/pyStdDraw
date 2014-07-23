#-----------------------------------------------------------------------
# bernoulli.py
#-----------------------------------------------------------------------

import sys
import math
import stdrandom
import stdstats
import stddraw
import gaussian

#-----------------------------------------------------------------------

# Simulating flipping a coin n times. Return the number of heads.

def binomial(n):
    heads = 0
    for i in range(n):
        if stdrandom.bernoulli(0.5):
            heads += 1
    return heads

#-----------------------------------------------------------------------

# Accept array argv containing integers n and t. Perform t experiments,
# each of which counts the number of heads found when a fair coin is
# flipped n times. Then draw the results to stddraw. Also draw the
# predicted Gaussian distribution function, thereby allowing easy
# comparison of the experimental results to the theoretically
# predicted results.

def main(argv):

    n = int(argv[1])
    t = int(argv[2])
    stddraw.createWindow()
    stddraw.setYscale(0, 0.2)

    freq = [0] * (n+1)
    for t in range(t):
        freq[binomial(n)] += 1

    norm = [0.0] * (n+1)
    for i in range(n+1):
        norm[i] = float(freq[i]) / float(t)
    stdstats.plotBars(norm)

    stddev = math.sqrt(n) / 2.0
    phi = [0.0] * (n+1)
    for i in range(n+1):
        phi[i] = gaussian.phi(i, n/2.0, stddev)

    stdstats.plotLines(phi)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
