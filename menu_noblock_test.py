import os
import sys

import pygame
from pygame.locals import *

progname = sys.argv[0]
progdir = os.path.dirname(progname)
sys.path.append(os.path.join(progdir,'gamelib'))

from popup_menu import NonBlockingPopupMenu
import stddrawpygame as stddraw 
stddraw.createWindow()
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx = .480
ry = .860
vx = .015
vy = .023

radius = .05
dt = 20

## Menu data and functions.
global menu_data
global _surface
menu_data = (
    'Main',
    'Save',
    'Quit',

)

menu = NonBlockingPopupMenu(menu_data)

def handle_menu(e):
    global menu
    print 'Menu event: %s.%d: %s' % (e.name,e.item_id,e.text)
    if e.name is None:
        print 'Hide menu'
        menu.hide()
    elif e.name == 'Main':
        print 'I am in the menu'
        if e.text == 'Save':
            print 'I hit save'
            stddraw.save(_surface)
        elif e.text == 'Quit':
            quit()

## Main loop.

while 1:
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

    stddraw.show(dt)
    
    
    # If the menu is visible it will be drawn.
    menu.draw()
    pygame.display.flip()

    # Pass them through the menu. If the menu is visible it will consume mouse
    # events and return any unhandled events; else it will return them all.
    # Process the unhandled events returned by the menu. Function handle_menu()
    # processes only events posted by the menu.
    for e in menu.handle_events(pygame.event.get()):
        if e.type == KEYDOWN:
            print 'Key pressed:',pygame.key.name(e.key)
        elif e.type == MOUSEBUTTONUP:
            print 'Show menu'
            menu.show()
        elif e.type == USEREVENT:
            if e.code == 'MENU':
                print 'handle menu is called'
                handle_menu(e)
    
