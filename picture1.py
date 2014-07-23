
"""
picture.py

The picture module defines the Picture class and the wait() function.
"""

#-----------------------------------------------------------------------

import sys
import pygame
import color
import tkintercommon
import stdarray

#-----------------------------------------------------------------------

_DEFAULT_SIZE = 512

#-----------------------------------------------------------------------

def wait():
    """
    Wait for the user to close this application's primary window.
    """
    tkintercommon.wait()

#-----------------------------------------------------------------------

class Picture:
    """
    A Picture object models an image.  It is initialized such that
    it has a given width and height and contains all black pixels.
    Subsequently you can load an image from a given GIF or JPG file.
    """


    #Fields:
    #   _photoImage:
    #       The image to be displayed.
    #   _buffer:
    #       An array of colors. For efficiency, get() and put() use
    #       _buffer instead of _photoImage. show() copies _buffer to
    #       _photoImage when the two differ.
    #   _isDirty:
    #       Set to True iff _buffer differs from _photoImage.
    #   _toplevel:
    #       The Tkinter Toplevel object in which this Picture
    #       will be displayed.
    #   _label:
    #       The Tkinter Label object in which this Picture will
    #       be displayed.
    _count = 0
    def __init__(self, maxW=_DEFAULT_SIZE, maxH=_DEFAULT_SIZE):
        """
        Construct 'self' such that it is all black with width 'maxW'
        and height 'maxH'.
        """
        if _count == 0:
            _background = pygame.display.set_mode([w, h + 50])
            self._photoImage = pygame.Surface((w, h))
            self._photoImage.fill(pygameColor(BLACK))
        else:
            self._photoImage = pygame.Surface((w, h))

            
        count += 1

        self._photoImage = None
        self._buffer = None
        self._isDirty = None
        self._toplevel = None
        self._label = None

        self._photoImage = \
            Tkinter.PhotoImage(width=maxW, height=maxH)
        self._buffer = \
            stdarray.create2D(maxW, maxH, str(color.BLACK))
        self._isDirty = True


    def load(self, f):
        """
        Load an image from the file whose name is 'f'. 'f' can be a
        JPG file or a PNG file.
        """
        self._photoImage = pygame.image.load(f)
        _background.blit(self._photoImage, (0,0))
        else:
            raise Exception('Unrecognized file type')

    #-------------------------------------------------------------------

    def width(self):
        """
        Return the width of 'self'.
        """
        return len(self._buffer)

    #-------------------------------------------------------------------

    def height(self):
        """
        Return the height of 'self'.
        """
        return len(self._buffer[0])

    #-------------------------------------------------------------------

    def get(self, w, h):
        """
        Return the color of 'self' at location ['w', 'h']
        """
        colorStr = self._buffer[w][h]
        r = int(colorStr[1:3], 16)  # Red component
        g = int(colorStr[3:5], 16)  # Green component
        b = int(colorStr[5:], 16)   # Blue component
        return color.Color(r, g, b)

    #-------------------------------------------------------------------

    def set(self, w, h, color):
        """
        Set the color of 'self' at location ['w', 'h'] to 'color'.
        """
        self._buffer[w][h] = str(color)
        self._isDirty = True

    #-------------------------------------------------------------------

    def show(self):
        """
        Render 'self' to its window.
        """
        try:
            # If the buffer has been changed since the last call of
            # show(), then copy the buffer to the image.
            if self._isDirty:

                # Create a string that expresses the colors in the odd
                # format that image.put() requires.
                maxH = self.height()
                maxW = self.width()
                colorStr = ''
                for h in range(maxH):
                    colorStr += '{'
                    for w in range(maxW):
                        colorStr += self._buffer[w][h] + ' '
                    colorStr += '} '

                # Copy the string to the image.
                self._photoImage.put(colorStr, (0, 0))
                self._isDirty = False

            # Each Picture is rendered via a distinct Toplevel object.
            # The first Picture that is rendered uses the root Toplevel
            # object, if it's available. Each subsequently rendered
            # Picture uses a secondary TopLevel object.
            if self._toplevel == None:
                if not tkintercommon.rootUsed:
                    self._toplevel = tkintercommon.root
                    tkintercommon.rootUsed = True
                else:
                    self._toplevel = Tkinter.Toplevel()
                self._toplevel.title('Picture Window')
                self._label = Tkinter.Label(self._toplevel)
                self._label.pack()

                # Define a listener for the 'Save' menu item.
                def saveListener():
                    FILE_TYPES = [('PPM File','*.ppm'),
                        ('Any File','*')]
                    f = tkFileDialog.asksaveasfilename(
                        defaultextension='.ppm',
                        filetypes=FILE_TYPES)
                    self._photoImage.write(f, 'ppm')

                # Create a menu containing a 'Save' menu item.
                self._saveMenu = Tkinter.Menu()
                self._saveMenu.add_command(label='Save...',
                    command=saveListener)
                self._saveMenu['tearoff'] = 0
                self._menubar = Tkinter.Menu()
                self._menubar.add_cascade(label='File',
                    menu=self._saveMenu)
                self._toplevel['menu'] = self._menubar

            self._label.config(image=self._photoImage)
            self._toplevel.update()

        except Tkinter.TclError:
            sys.exit(0)
