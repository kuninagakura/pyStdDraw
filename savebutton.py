import os
import sys
import pygame
import stddrawpygame as stddraw
import string
from pygame.locals import *

#----------Button checker--------------------------------
def _checkButtonX(mousePoints, buttonWidth):
    return (mousePoints[0] > 290 and mousePoints[0] < 290 + buttonWidth)

def _checkButtonY(mousePoints, buttonHeight):
    return (mousePoints[1] > 10 and mousePoints[1] < 10 + buttonHeight)

def checkButton():
    global button
    mousePoints = pygame.mouse.get_pos()
    buttonWidth = button.get_width()
    buttonHeight = button.get_height()
    if (_checkButtonX(mousePoints, buttonWidth) and _checkButtonY(mousePoints, buttonHeight)):
        return True
#---------------------------------------------------------


#----------InputBox checker--------------------------------
def _checkInputBoxX(mousePoints, InputBoxWidth):
    return (mousePoints[0] > 12 and mousePoints[0] < 12 + InputBoxWidth)

def _checkInputBoxY(mousePoints, InputBoxHeight):
    return (mousePoints[1] > 12 and mousePoints[1] < 12 + InputBoxHeight)

def checkInputBox():
    print 'checkInputBox()'
    mousePoints = pygame.mouse.get_pos()
    InputBoxWidth = 255
    InputBoxHeight = 25
    if (_checkInputBoxX(mousePoints, InputBoxWidth) and _checkInputBoxY(mousePoints, InputBoxHeight)):
        return True
#---------------------------------------------------------

def circle(x, y, r):
    """
    Draw on the surface a circle of radius r centered on (x, y).
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
            stddraw.pygameColor(stddraw.BLACK),
            pygame.Rect(xs-ws/2, ys-hs/2, ws, hs), 1
            )

def display_buttonBackground(_background, message, pressed, inputPressed):
    global button
    global buttonBackground
    #initialize font
    pygame.font.init()
    fontobject = pygame.font.Font(None, 18)

    #create buttonBackground surface and load the button image
    buttonBackground = pygame.Surface((512, 50))
    buttonBackground.fill(stddraw.pygameColor(stddraw.RED))
    button = pygame.image.load(os.path.join( 'saveIcon.png'))
    #check to see if the button is pressed
    if pressed:
        button.fill(stddraw.pygameColor(stddraw.LIGHT_GRAY))
    
    pygame.draw.line(buttonBackground, stddraw.pygameColor(stddraw.BLACK), (0, 49), (511, 49))
    pygame.draw.rect(buttonBackground, stddraw.pygameColor(stddraw.BLACK),
                   (10, 10,
                    260, 30), 0)
    pygame.draw.rect(buttonBackground, stddraw.pygameColor(stddraw.WHITE),
                   (12, 12,
                    255, 25), 0)
    if inputPressed:
        pygame.draw.rect(buttonBackground, stddraw.pygameColor(stddraw.BOOK_BLUE),
                   (10, 10,
                    259, 29), 2)

    if len(message) != 0:
        buttonBackground.blit(fontobject.render(message, 1, stddraw.pygameColor(stddraw.BLACK)), 
            (15, 20))
    buttonBackground.blit(button, (290, 10))
    _background.blit(buttonBackground, (0, 0))

    pygame.display.flip()
    return buttonBackground

def get_name(_background):
    global _surface
    global current_string 
    global buttonBackground

    current_string = []
    inputSelect = False
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            if inputSelect:
                inkey = event.key
                if inkey == K_BACKSPACE:
                    current_string = current_string[0:-1]
                elif inkey == K_MINUS:
                    current_string.append("_")
                elif inkey <= 127:
                    current_string.append(chr(inkey))
        elif event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if checkButton():
                display_buttonBackground(_background, string.join(current_string, ""), True, inputSelect)
        elif event.type == MOUSEBUTTONUP:
            if checkButton():
                pygame.image.save(_surface, ''.join(current_string) + ".JPEG")
            inputSelect = checkInputBox()        
        display_buttonBackground(_background, string.join(current_string, ""), False, inputSelect)
    return string.join(current_string, "")

def main():
    ## Main loop.
    global _surface
    global _background

    _background = pygame.display.set_mode([512, 562])
    _surface = pygame.Surface((512, 512))
    _surface.fill(stddraw.pygameColor(stddraw.WHITE))
    circle(0.5, 0.5, 0.5)
    _background.blit(_surface, (0, 50))
    display_buttonBackground(_background, "", False, False)

    name = get_name(_background) 

    print name + " was entered"
    
    
    # Update ball position and draw it there.

if __name__ == '__main__': main()
