#-----------------------------------------------------------------------
# body.py
#-----------------------------------------------------------------------

import vector
import stddraw

class Body:

    def __init__(self, r, v, mass):
        self._r = r        # Position
        self._v = v        # Velocity
        self._mass = mass  # Mass

    def move(self, f, dt):
        a = f * (1 / self._mass)
        self._v = self._v + (a * dt)
        self._r = self._r + (self._v * dt)

    def forceTo(self, b):
        a = self
        G = 6.67e-11
        delta = a._r - b._r
        dist = abs(delta)
        F = (G * a._mass * b._mass) / (dist * dist)
        return delta.direction() * F

    def draw(self):
        stddraw.setPenRadius(0.025)
        stddraw.point(self._r.cartesian(0), self._r.cartesian(1))
