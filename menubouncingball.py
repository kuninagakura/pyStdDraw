#-----------------------------------------------------------------------
# menubouncingball.py
#-----------------------------------------------------------------------

import os
import sys
import pygame
from pygame.locals import *

import stddrawpygame as stddraw
from popup_menu import PopupMenu

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

#--menu stuff--
global menu_data
global _surface
menu_data = (
    'Main',
    'Save',
    'Quit',
)
def handle_menu(e):
    print 'Menu event: %s.%d: %s' % (e.name,e.item_id,e.text)
    if e.name == 'Main':
        if e.text == 'Save':
            stddraw.save(_surface)
        if e.text == 'Quit':
            quit()

while True:
    #--menu stuff--
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == MOUSEBUTTONUP:
            ## Blocking popup menu.
            PopupMenu(menu_data)
        elif e.type == USEREVENT:
            if e.code == 'MENU':
                handle_menu(e)
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

