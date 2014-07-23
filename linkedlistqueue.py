#-----------------------------------------------------------------------
# linkedlistqueue.py
#   python linkedlistqueue.py < tobe.txt
#-----------------------------------------------------------------------

# A Queue object is a first-in-first-out container.

class Queue:

    #-------------------------------------------------------------------

    # A _Node object references an item and a next _Node object.
    # A Queue object is composed of _Node objects.

    class _Node:
        def __init__(self, item, next):
            self.item = item  # Reference to an item
            self.next = next  # Reference to the next _Node object

    #-------------------------------------------------------------------

    # Construct 'self' as an empty Queue object.

    def __init__(self):
        self._first = None  # Reference to first _Node
        self._last = None   # Reference to last _Node
        self._length = 0    # Number of items

    #-------------------------------------------------------------------

    # Return True iff 'self' is empty.

    def isEmpty(self):
        return self._length == 0

    #-------------------------------------------------------------------

    # Add 'item' to the end of 'self'.

    def enqueue(self, item):
        oldLast = self._last
        self._last = Queue._Node(item, None)
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast.next = self._last
        self._length += 1

    #-------------------------------------------------------------------

    # Remove the first item of 'self' and return it.

    def dequeue(self):
        item = self._first.item
        self._first = self._first.next
        if self.isEmpty():
            self._last = None
        self._length -= 1
        return item

    #-------------------------------------------------------------------

    # Return the number of items in 'self'.

    def __len__(self):
        return self._length

    #-------------------------------------------------------------------

    # Return a string representation of 'self'.

    def __str__(self):
        s = ''
        cur = self._first
        while cur != None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s

    #-------------------------------------------------------------------

    # An _Iterator object iterates over a Queue object.

    class _Iterator:

        #---------------------------------------------------------------

        # Construct an _Iterator object for 'queue'.

        def __init__(self, queue):
            self._cur = queue._first

        #---------------------------------------------------------------

        # Return the current item of the associated Queue object, and
        # advance 'self' to the next item.

        def next(self):
            if self._cur == None:
                raise StopIteration()
            item = self._cur.item
            self._cur = self._cur.next
            return item

        #---------------------------------------------------------------

        # Python 3.x requires __next__() instead of next().

        __next__ = next

    #-------------------------------------------------------------------

    # Return an iterator for 'self'.

    def __iter__(self):
        return Queue._Iterator(self)

#-----------------------------------------------------------------------

# For testing:

def main():

    import stdio

    q = Queue()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            q.enqueue(item)
        else:
            stdio.writeln(q.dequeue())

    stdio.writeln('Iterating over the queue')
    for item in q:
        stdio.writeln(item)

    stdio.writeln('Printing the queue as a string')
    stdio.writeln(q)

    stdio.writeln('Emptying the queue')
    while not q.isEmpty():
        stdio.writeln(q.dequeue())

if __name__ == '__main__':
    main()
