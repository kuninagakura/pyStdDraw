#-----------------------------------------------------------------------
# loadbalance.py
#-----------------------------------------------------------------------

import sys
import stddraw
import stdstats
import linkedlistqueue
import randomqueue

def main(argv):
    M = int(argv[1])
    N = int(argv[2])
    S = int(argv[3])

    # Create a RandomQueue object containing Queue objects.
    servers = randomqueue.RandomQueue()
    for i in range(M):
        servers.enqueue(linkedlistqueue.Queue())

    for j in range(N):
        # Assign an item to a server.
        min = servers.sample()
        for k in range(1, S):
            # Pick a random server, update if new min.
            q = servers.sample()
            if len(q) < len(min):
                min = q
        # min is the shortest server queue.
        min.enqueue(j)

    lengths = []
    for q in servers:
        lengths += [len(q)]
    stddraw.createWindow()
    stddraw.setYscale(0, 2.0*N/M)
    stdstats.plotBars(lengths)
    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)

#-----------------------------------------------------------------------

# Sample executions:

# python loadbalance.py 50 500 1
# python loadbalance.py 50 500 2
