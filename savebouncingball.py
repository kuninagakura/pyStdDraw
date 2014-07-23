import os
import sys
import pygame
import stddrawpygame as stddraw
import string
import thread

from pygame.locals import *
global _surface
global _deferDraw

def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key 
        else:
            pass
#----stddraw functions we need for now
   
def _draw():
    """
    Update the surface on the window if deferDraw is False.
    """
    if not _deferDraw:
        pygame.display.flip()
        checkForEvents()

def show(t=None):
    """
    Update the surface on the window.  If t is given, defer subsequent updates
    for t milliseconds.
    """
    global _deferDraw
    _deferDraw = False
    _draw()
    if t != None:
        time.sleep(float(t) / 1000.0)
        _deferDraw = True
def filledSquare(x, y, r):
    global _surface
    """
    Draw on the surface a filled square whose sides are of length 2r,
    centered on (x, y).
    """
    ws = stddraw._factorX(2*r)
    hs = stddraw._factorY(2*r)
    if (ws <= 1) and (hs <= 1):
        stddraw._pixel(x, y)
    else:
        xs = stddraw._scaleX(x)
        ys = stddraw._scaleY(y)    
        filledRectangle(x, y, r, r)

def filledRectangle(x, y, w, h):
    """
    Draw on the surface a filled rectangle of width w and height h,
    centered on (x, y).
    """
    global _surface
    ws = stddraw._factorX(2*w)
    hs = stddraw._factorY(2*h)
    if (ws <= 1) and (hs <= 1):
        stddraw._pixel(x, y)
    else:
        xs = stddraw._scaleX(x)
        ys = stddraw._scaleY(y)
        pygame.draw.rect(_surface,
            pygameColor(stddraw.pygameColor(stddraw.GRAY)),
            pygame.Rect(xs-ws/2, ys-hs/2, ws, hs),
            0)
        _draw()
def filledCircle(x, y, r):
    """
    Draw on the surface a filled circle of radius r centered on (x, y).
    """
    global _surface
    ws = stddraw._factorX(2*r)
    hs = stddraw._factorY(2*r)
    if (ws <= 1) and (hs <= 1):
        stddraw._pixel(x, y)
    else:
        xs = stddraw._scaleX(x)
        ys = stddraw._scaleY(y)
        pygame.draw.ellipse(_surface,
            stddrawpygameColor(stddraw.BLACK),
            pygame.Rect(xs-ws/2, ys-hs/2, ws, hs),
            0)
        _draw()

#-------
def display_buttonBackground(_background, message):
    pygame.font.init()
    fontobject = pygame.font.Font(None, 18)
    buttonBackground = pygame.Surface((512, 50))
    buttonBackground.fill(stddraw.pygameColor(stddraw.RED))
    button = pygame.Surface((80, 30))

    button.fill(stddraw.pygameColor(stddraw.GRAY))
    button.blit(fontobject.render("Save", 1, (0,0,0)), (button.get_width() / 2 - 20, button.get_height() / 2 - 5))
        
    pygame.draw.line(buttonBackground, stddraw.pygameColor(stddraw.BLACK), (0, 49), (511, 49))
    pygame.draw.rect(buttonBackground, stddraw.pygameColor(stddraw.BLACK),
                   (10, 10,
                    260, 30), 0)
    pygame.draw.rect(buttonBackground, stddraw.pygameColor(stddraw.WHITE),
                   (12, 12,
                    255, 25), 0)
    if len(message) != 0:
        print "should be printing words"
        buttonBackground.blit(fontobject.render(message, 1, stddraw.pygameColor(stddraw.BLACK)), 
            (15, 20))
    buttonBackground.blit(button, (290, 10))
    _background.blit(buttonBackground, (0, 0))
    pygame.display.flip()
    return buttonBackground

def get_name(_background):
    global _surface
    pygame.font.init()
    current_string = []
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            pygame.image.save(_surface, ''.join(current_string)+ ".JPEG")
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        
        display_buttonBackground(_background, string.join(current_string, ""))
    return string.join(current_string, "")

def window( threadName, delay):
    ## Main loop.
    global _surface

    _background = pygame.display.set_mode([512, 562])
    _surface = pygame.Surface((512, 512))
    _surface.fill(stddraw.pygameColor(stddraw.WHITE))
    _background.blit(_surface, (0, 50))
    display_buttonBackground(_background, "")

    name = get_name(_background) 

    print name + " was entered"
def bouncingBall( threadName, delay):
    global _surface    
    stddraw.setXscale(-1.0, 1.0)
    stddraw.setYscale(-1.0, 1.0)

    rx = .480
    ry = .860
    vx = .015
    vy = .023

    radius = .05
    dt = 20


    while True:
        # Update ball position and draw it there.
        if abs(rx + vx) + radius > 1.0:
            vx = -vx
        if abs(ry + vy) + radius > 1.0:
            vy = -vy
        rx = rx + vx
        ry = ry + vy


        filledSquare(0, 0, 1.0)

        filledCircle(rx, ry, radius)

        show(dt)
        
    # Update ball position and draw it there.

def main():
    try: 
        thread.start_new_thread( window, ("Thread-1", 2, ) )
        thread.start_new_thread( bouncingBall, ("Thread-2", 4, ) )
    except:
        print "Error: unable to start thread"
    while 1:
        pass

if __name__ == '__main__': main()
