#-----------------------------------------------------------------------
# guitarstring.py
#   python guitarstring.py 100
#-----------------------------------------------------------------------

import random
import collections

_SAMPLE_RATE = 44100
_DECAY_FACTOR = 0.996
_FAINT_TIME = 150000

class GuitarString:

    # Construct a guitar string representing the given frequency or
    # with the given array.
    def __init__(self, init):
        self._time = 0
        self._queue = collections.deque()
        if isinstance(init, float):
            n = int(round(_SAMPLE_RATE / init))
            for i in range(n):
                self._queue.append(0.0)
        elif isinstance(init, list):
            for i in range(len(init)):
                self._queue.append(init[i]);
        else:
            raise Exception('Invalid arg to GuitarString constructor')

    # Pluck the string.  Excite with white noise between -0.5 and 0.5.
    def pluck(self):
        self._time = 0
        length = len(self._queue)
        for i in range(length):
            self._queue.popleft()
            self._queue.append(random.uniform(-0.5, 0.5))

    # Advance the simulation one step.
    def tic(self):
        self._time += 1
        current = self._queue.popleft()
        next = self._queue[0]
        self._queue.append(_DECAY_FACTOR * (current + next) / 2.0)

    # Return the current sample.
    def sample(self):
        return self._queue[0]

    # Return True iff the string is faint.
    def isFaint(self):
        return self._time > _FAINT_TIME

    # Return the number of time steps (that is, the number of calls
    # to tic().
    def time(self):
        return self._time

#-----------------------------------------------------------------------

# For testing:

def main1(argv):
    import stdio
    N = int(argv[1])
    samples = [ .2, .4, .5, .3, -.2, .4, .3, -.5, -.1, -.3 ]
    test = GuitarString(samples)
    for i in range(N):
        t = test.time()
        sample = test.sample()
        stdio.writef("%6d %8.4f\n", t, sample)
        test.tic()

def main2():
    import stddraw
    import stdaudio

    #stddraw.setXscale(0, 1024)
    #stddraw.setYscale(-1, +1)
    #stddraw.show(0)

    # Play middle A for 3 seconds.
    a = GuitarString(440.0)
    a.pluck()
    seconds = 3
    for i in range(_SAMPLE_RATE * seconds):
        a.tic()
        stdaudio.playSample(a.sample())
        #stddraw.point(i % 1024, a.sample())
        #if i % 1024 == 1023:
        #    stddraw.show(0)
        #    stddraw.clear()

if __name__ == '__main__':
    import sys
    main1(sys.argv)
    main2()
