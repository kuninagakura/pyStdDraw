"""
stdrandom.py

The stdrandom module defines functions related to pseudo-random
numbers.
"""

#-----------------------------------------------------------------------

import random
import math

#-----------------------------------------------------------------------

def uniformInt(lo, hi):
    """
    Return an integer uniformly in ['lo', 'hi'), where 'lo' and 'hi'
    are integers.
    """
    # Or instead call random.randrange(lo, hi) directly.
    return random.randrange(lo, hi)

#-----------------------------------------------------------------------

def uniformFloat(lo, hi):
    """
    Return a float uniformly in ['lo', 'hi'), where 'lo' and 'hi'
    are floats.
    """
    # Or instead call random.uniform(lo, hi) directly.
    return random.uniform(lo, hi)

#-----------------------------------------------------------------------

def bernoulli(p):
    """
    Return True with probability 'p'.
    """
    # Or instead call scipy.stats.bernoulli().
    return random.random() < p

#-----------------------------------------------------------------------

def gaussian(mean=0.0, stddev=1.0):
    """
    Return a float according to a standard Gaussian distribution
    with the given mean ('mean') and standard deviation ('stddev').
    """

    # Or instead call random.gauss(mu, sigma).

    # Use the polar form of the Box-Muller transform.
    x = uniformFloat(-1.0, 1.0)
    y = uniformFloat(-1.0, 1.0)
    r = x*x + y*y
    while (r >= 1) or (r == 0):
        x = uniformFloat(-1.0, 1.0)
        y = uniformFloat(-1.0, 1.0)
        r = x*x + y*y
    g = x * math.sqrt(-2 * math.log(r) / r)
    # Remark:  x * math.sqrt(-2 * math.log(r) / r)
    # is an independent random gaussian
    return mean + stddev * g

#-----------------------------------------------------------------------

def discrete(a):
    """
    Return a float from a discrete distribution: i with probability
    a[i].  Precondition: the elements of array 'a' sum to 1.
    """
    r = uniformFloat(0.0, 1.0)
    sum = 0.0
    for i in range(len(a)):
        sum += a[i]
        if sum > r:
            return i
    return len(a) -1

#-----------------------------------------------------------------------

def shuffle(a):
    """
    Shuffle array 'a'.
    """
    # Or instead call random.shuffle(a) directly.
    random.shuffle(a)

#-----------------------------------------------------------------------

def exp(lambd):
    """
    Return a float from an exponential distribution with rate 'lambd'.
    """
    # Or instead call random.expovariate(lambd)
    return -math.log(1 - random.random()) / lambd

#-----------------------------------------------------------------------

def main(argv):
    """
    For testing:
    """
    import stdio
    N = int(argv[1])
    t = [.5, .3, .1, .1]
    for i in range(N):
        stdio.writef(' %2d ' , uniformInt(-100, 100))
        stdio.writef('%8.5f ', uniformFloat(10.0, 99.0))
        if bernoulli(.5):
            stdio.write('False ')
        else:
            stdio.write('True  ')
        stdio.writef('%7.5f ', gaussian(9.0, .2))
        stdio.writef('%2d '  , discrete(t))
        stdio.writeln()

if __name__ == '__main__':
    import sys
    main(sys.argv)