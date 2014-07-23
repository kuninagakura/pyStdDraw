#-----------------------------------------------------------------------
# universe.py
#   python universe.py 20000 < 2bodyTiny.txt
#   python universe.py 20000 < 2body.txt
#   python universe.py 20000 < 3body.txt
#   python universe.py 20000 < 4body.txt
#-----------------------------------------------------------------------

import stdio
import vector
import sys
import stddraw
import body

#-----------------------------------------------------------------------

class Universe:

    # read universe from standard input
    def __init__(self):

        self._N = stdio.readInt()         # Number of bodies
        self._radius = stdio.readFloat()  # Radius of universe

        # the set scale for drawing on screen
        stddraw.setXscale(-self._radius, +self._radius)
        stddraw.setYscale(-self._radius, +self._radius)

        # read in the _N bodies
        self.orbs = []  # Array of bodies
        for i in range(self._N):
            rx   = stdio.readFloat()
            ry   = stdio.readFloat()
            vx   = stdio.readFloat()
            vy   = stdio.readFloat()
            mass = stdio.readFloat()
            position = [ rx, ry ]
            velocity = [ vx, vy ]
            r = vector.Vector(position)
            v = vector.Vector(velocity)
            self.orbs += [body.Body(r, v, mass)]

    # increment time by dt units, assume forces are constant
    # in given interval
    def increaseTime(self, dt):

        # initialize the forces to zero
        f = []
        for i in range(self._N):
            f += [vector.Vector([0.0, 0.0])]

        # compute the forces
        for i in range(self._N):
            for j in range(self._N):
                if i != j:
                    f[i] = f[i] + self.orbs[j].forceTo(self.orbs[i])

        # move the bodies
        for i in range(self._N):
            self.orbs[i].move(f[i], dt)

    # draw the _N bodies
    def draw(self):
        for i in range(self._N):
            self.orbs[i].draw()

#-----------------------------------------------------------------------

# Simulate a universe

def main(argv):
    stddraw.createWindow()
    newton = Universe()
    dt = float(argv[1])
    while True:
        newton.increaseTime(dt)
        newton.draw()
        stddraw.sleep(10)
        stddraw.show()
        stddraw.clear()
        
if __name__ == '__main__':
    main(sys.argv)
