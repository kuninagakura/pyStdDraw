#-----------------------------------------------------------------------
# gaussian.py
#-----------------------------------------------------------------------

import math

#-----------------------------------------------------------------------

def _phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

#-----------------------------------------------------------------------

# Return Gaussian pdf with mean mu and stddev sigma.

def phi(x, mu=0.0, sigma=1.0):
    return _phi((x - mu) / sigma) / sigma

#-----------------------------------------------------------------------

def _Phi(z):
    if z < -8.0: return 0.0
    if z >  8.0: return 1.0
    sum = 0.0
    term = z
    i = 3
    while sum != sum + term:
        sum += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + sum * phi(z)

#-----------------------------------------------------------------------

# Return standard Gaussian cdf with mean mu and stddev sigma.
# Use Taylor approximation.

def Phi(z, mu=0.0, sigma=1.0):
    return _Phi((z - mu) / sigma)

#-----------------------------------------------------------------------

def _PhiInverse(y, delta, lo, hi):
    mid = lo + ((hi - lo) / 2.0)
    if (hi - lo) < delta:
        return mid
    if Phi(mid) > y:
        return _PhiInverse(y, delta, lo, mid)
    else:
        return _PhiInverse(y, delta, mid, hi)

#-----------------------------------------------------------------------

# Return x such that Phi(x) = y.

def PhiInverse(y):
    return _PhiInverse(y, .00000001, -8.0, 8.0)

#-----------------------------------------------------------------------

# For testing:

def main(argv):

    import stdio

    z = float(argv[1])
    mu = float(argv[2])
    sigma = float(argv[3])

    stdio.writeln(Phi((z - mu) / sigma))
    stdio.writeln(Phi(z, mu, sigma));
    y = Phi(z);
    stdio.writeln(PhiInverse(y));

if __name__ == '__main__':
    import sys
    main(sys.argv)
