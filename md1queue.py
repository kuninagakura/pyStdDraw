#-----------------------------------------------------------------------
# md1queue.py
#-----------------------------------------------------------------------

import sys
import linkedlistqueue
import stddraw
import stdrandom
import histogram

def main(argv):

    lamb = float(argv[1])  # Arrival rate
    mu = float(argv[2])    # Service rate

    hist = histogram.Histogram(60 + 1)
    q = linkedlistqueue.Queue()
    stddraw.createWindow(700, 500)

    nextArrival = stdrandom.exp(lamb)  # Time of next arrival
    nextService = nextArrival + 1.0/mu # Time of next completed service

    # Simulate the M/D/1 queue
    while True:

        # Next event is an arrival.
        while nextArrival < nextService:
            # Simulate an arrival
            q.enqueue(nextArrival)
            nextArrival += stdrandom.exp(lamb)

        # Next event is a service completion.
        arrival = q.dequeue()
        wait = nextService - arrival

        # Update the histogram.
        stddraw.clear()
        hist.addDataPoint(min([60, int(wait+0.5)]))
        hist.draw()
        #stddraw.sleep(20)
        stddraw.sleep(20)
        stddraw.show()
        # Update the queue.
        if q.isEmpty():
            nextService = nextArrival + 1.0/mu
        else:
            nextService = nextService + 1.0/mu

if __name__ == '__main__':
    main(sys.argv)

#-----------------------------------------------------------------------

# Example executions:

# python md1queue.py .167 .25
# python md1queue.py .167 .22

