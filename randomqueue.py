#-----------------------------------------------------------------------
# randomqueue.py
#   python randomqueue.py < tobe.txt
#-----------------------------------------------------------------------

import stdrandom

#-----------------------------------------------------------------------

# A RandomQueue object is a collection whose items are in random order.

class RandomQueue:

    #-------------------------------------------------------------------

    # Construct an empty RandomQueue object.

    def __init__(self):
        self._a = []  # Items

    #-------------------------------------------------------------------

    # Return True iff 'self' is empty.

    def isEmpty(self):
        return self._a == []

    #-------------------------------------------------------------------

    # Add 'item' to 'self'.

    def enqueue(self, item):
        self._a += [item]

    #-------------------------------------------------------------------

    # Remove and return a random item of 'self'.

    def dequeue(self):
        length = len(self._a)
        r = stdrandom.uniformInt(0, length)
        self._a[length-1], self._a[r] = self._a[r], self._a[length-1]
        return self._a.pop()

    #-------------------------------------------------------------------

    # Return a random item of 'self'.

    def sample(self):
        length = len(self._a)
        r = stdrandom.uniformInt(0, length)
        return self._a[r]

    #-------------------------------------------------------------------

    # Return the number of items in 'self'.

    def __len__(self):
        return len(self._a)

    #-------------------------------------------------------------------

    # Return a string representation of 'self'.

    def __str__(self):
        a = list(self._a)  # Make a copy
        stdrandom.shuffle(a)  # Shuffle it.
        s = ''
        for item in a:
            s += str(item) + ' '
        return s

    #-------------------------------------------------------------------

    # An _Iterator object iterates over a RandomQueue object.

    class _Iterator:

        #---------------------------------------------------------------

        # Construct an _Iterator object for 'randomQueue'.

        def __init__(self, randomQueue):
            self._a = list(randomQueue._a)  # Make a copy.
            stdrandom.shuffle(self._a)      # Shuffle it.
            self._i = 0

        #---------------------------------------------------------------

        # Return the current item of the associated Stack object, and
        # advance 'self' to the next item.

        def __next__(self):
            if self._i >= len(self._a):
                raise StopIteration()
            item = self._a[self._i]
            self._i += 1
            return item

        #---------------------------------------------------------------

        # Python 2.x requires next() instead of __next__().

        next = __next__

    #-------------------------------------------------------------------

    # Return an iterator for 'self'.

    def __iter__(self):
        return RandomQueue._Iterator(self)

#-----------------------------------------------------------------------

# For testing:

def main():

    import stdio

    q = RandomQueue()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            q.enqueue(item)
        else:
            stdio.writeln(q.dequeue())

    stdio.writeln('Iterate over all remaining items')
    for item in q:
        stdio.writeln(item)

    stdio.writeln('Printing a string rep of the remaining items')
    stdio.writeln(q)

    stdio.writeln('Empty the random queue')
    while not q.isEmpty():
        stdio.writeln(q.dequeue())

if __name__ == '__main__':
    main()
