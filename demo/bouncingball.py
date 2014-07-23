#-----------------------------------------------------------------------
# bouncingball.py
#-----------------------------------------------------------------------
import time
#import stddrawtkinter as stddraw
import stddraw
# Draw a bouncing ball.
stddraw.createWindow()
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx = .480
ry = .860
vx = .015
vy = .023

radius = .05
dt = 20
start = time.time()

t = 0
while t < 10000:
    # Update ball position and draw it there.
    if abs(rx + vx) + radius > 1.0:
        vx = -vx
    if abs(ry + vy) + radius > 1.0:
        vy = -vy
    rx = rx + vx
    ry = ry + vy
    
    #stddraw.clear()

    stddraw.setPenColor(stddraw.GRAY)
    stddraw.filledSquare(0, 0, 1.0)

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(rx, ry, radius)

    #stddraw.sleep(dt)
    stddraw.show()
    t += 1
finish = time.time()

print finish - start
