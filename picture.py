"""
picture.py

The picture module defines the Picture class.
"""

#-----------------------------------------------------------------------

import pygame
import sys
import color
import stdarray

#-----------------------------------------------------------------------

_DEFAULT_WIDTH = 512
_DEFAULT_HEIGHT = 512

#-----------------------------------------------------------------------

class Picture:
    """
    A Picture object models an image.  It is initialized such that
    it has a given width and height and contains all black pixels.
    Subsequently you can load an image from a given JPG or PNG file.
    """
    def __init__(self, maxW=_DEFAULT_WIDTH, maxH=_DEFAULT_HEIGHT):
        """
        Construct self such that it is all black with width maxW
        and height maxH.
        """
        self._surface = pygame.Surface((maxW, maxH))
        self._surface.fill((0, 0, 0))

    #-------------------------------------------------------------------

    def load(self, f):
        """
        Change self by reading from the file whose name is f.
        """
        self._surface = pygame.image.load(f)

    #-------------------------------------------------------------------

    def save(self, f):
        """
        Save self to the file whose name is f.
        """
        pygame.image.save(self._surface, f)

    #-------------------------------------------------------------------

    def width(self):
        """
        Return the width of self.
        """
        return self._surface.get_width()

    #-------------------------------------------------------------------

    def height(self):
        """
        Return the height of self.
        """
        return self._surface.get_height()

    #-------------------------------------------------------------------

    def get(self, x, y):
        """
        Return the color of self at location (x, y).
        """
        pygameColor = self._surface.get_at((x, y))
        return color.Color(pygameColor.r, pygameColor.g, pygameColor.b)

    #-------------------------------------------------------------------

    def set(self, x, y, c):
        """
        Set the color of self at location (x, y) to c.
        """
        pygameColor = pygame.Color(c.getRed(), c.getGreen(),
           c.getBlue(), 0)
        self._surface.set_at((x, y), pygameColor)
