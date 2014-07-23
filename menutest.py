import os
import sys
import pygame
from pygame.locals import *

import stddrawpygame as stddraw
from popup_menu import PopupMenu



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

## Main loop.
stddraw.createWindow()
stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
stddraw.circle(0, 0, 0.5)
stddraw.show()
_surface = pygame.Surface.copy(stddraw._surface)

while 1:
    stddraw.clear()
    stddraw.circle(0, 0, 0.5)

    for e in pygame.event.get():
        if e.type == MOUSEBUTTONUP:
            ## Blocking popup menu.
            PopupMenu(menu_data)
        elif e.type == USEREVENT:
            if e.code == 'MENU':
                handle_menu(e)
    
    
    # Update ball position and draw it there.


