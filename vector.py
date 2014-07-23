#-----------------------------------------------------------------------
# vector.py
#-----------------------------------------------------------------------

import math

#-----------------------------------------------------------------------

class Vector:

    # Construct a new Vector object with numeric Cartesian coordinates
    # given in list a.
    def __init__(self, a):
        self._length = len(a) # Dimension.
        
        # Make a defensive copy to ensure immutability.
        self._coords = a[:]   # Cartesian coordinates

    # Return the sum of Vector objects self and other.
    def __add__(self, other):
        if self._length != other._length:
            raise Exception('Dimensions don\'t agree')
        sumCoords = []
        for i in range(self._length):
            sumCoords += [self._coords[i] + other._coords[i]]
        return Vector(sumCoords)

    # Return the difference of Vector objects self and other.
    def __sub__(self, other):
        if self._length != other._length:
            raise Exception('Dimensions don\'t agree')
        diffCoords = []
        for i in range(self._length):
            diffCoords += [self._coords[i] - other._coords[i]]
        return Vector(diffCoords)

    # Return the product of Vector object self and numeric object c.
    def __mul__(self, c):
        prodCoords = []
        for i in range(self._length):
            prodCoords += [c * self._coords[i]]
        return Vector(prodCoords)

    # Return the inner product of Vector objects self and other.
    def dot(self, other):
        if self._length != other._length:
            raise Exception('Dimensions don\'t agree')
        sum = 0.0
        for i in range(self._length):
            sum += self._coords[i] * other._coords[i]
        return sum

    # Return the magnitude, that is, the Euclidean norm, of Vector
    # object self.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of Vector object self.
    def direction(self):
        return self * (1.0 / abs(self))

    # Return the ith Cartesian coordinate of Vector object self.
    def cartesian(self, i):
        return self._coords[i]

    # Return a string representation of Vector object self.
    def __str__(self):
        s = '( '
        for coord in self._coords:
            s += str(coord) + ' '
        return s + ')'

#-----------------------------------------------------------------------

# For testing:

def main():

    import stdio

    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector(xCoords)
    y = Vector(yCoords)

    stdio.writeln('x        = ' + str(x))
    stdio.writeln('y        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('10x      = ' + str(x * 10.0))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))

if __name__ == '__main__':
    main()
