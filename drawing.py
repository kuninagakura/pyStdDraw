
"""
drawing.py

The drawing module defines the Drawing class and a wait() function.
As a convenience, it also imports the commonly used Color objects
defined in the color module.
"""

#-----------------------------------------------------------------------

import time
import sys
if sys.hexversion < 0x03000000:
    import Tkinter
    import tkFileDialog
else:
    import tkinter as Tkinter
    import tkinter.filedialog as tkFileDialog
import color
import tkintercommon

#-----------------------------------------------------------------------

# Define colors so clients need not import the color module.

from color import WHITE
from color import BLACK
from color import RED
from color import GREEN
from color import BLUE
from color import CYAN
from color import MAGENTA
from color import YELLOW
from color import DARK_RED
from color import DARK_GREEN
from color import DARK_BLUE
from color import GRAY
from color import DARK_GRAY
from color import LIGHT_GRAY
from color import ORANGE
from color import VIOLET
from color import PINK
from color import BOOK_BLUE
from color import BOOK_LIGHT_BLUE
from color import BOOK_RED

#-----------------------------------------------------------------------

def wait():
    """
    Wait for the user to close this application's primary window.
    """
    tkintercommon.wait()

#-----------------------------------------------------------------------

_BORDER = 0.05
_DEFAULT_XMIN = 0.0
_DEFAULT_XMAX = 1.0
_DEFAULT_YMIN = 0.0
_DEFAULT_YMAX = 1.0
_DEFAULT_SIZE = 512
_DEFAULT_PEN_RADIUS = .002
_DEFAULT_PEN_COLOR = color.BLACK

#-----------------------------------------------------------------------

class Drawing:

    """
    A Drawing object models a drawing, which is rendered on a canvas,
    which appears within a window.  Each Drawing object has its own
    distinct window.
    """

    def __init__(self):
        """
        Initialize self to a new Drawing object with an empty canvas.
        """

        self._width = _DEFAULT_SIZE
        self._height = _DEFAULT_SIZE
        self._penRadius = _DEFAULT_PEN_RADIUS
        self._penColor = _DEFAULT_PEN_COLOR

        self._xmin = None
        self._ymin = None
        self._xmax = None
        self._ymax = None
        self.setXscale()
        self.setYscale()

        # Should drawing be deferred?
        self._deferDraw = False

        # The Drawing object is rendered via a Toplevel object.
        # Use the root Toplevel object if it's available. Otherwise
        # create and use a new Toplevel object.
        if not tkintercommon.rootUsed:
            self._toplevel = tkintercommon.root
            tkintercommon.rootUsed = True
        else:
            self._toplevel = Tkinter.Toplevel()
            self._toplevel.title('Drawing Window')

        # Set the Toplevel object so it isn't resizable.
        self._toplevel.resizable(0, 0)

        # Create a Canvas object and place it in the Toplevel object,
        self._canvas = Tkinter.Canvas(self._toplevel,
            width=_DEFAULT_SIZE, height=_DEFAULT_SIZE)
        self._canvas.pack()

        # Define a listener for the 'Save' menu item.
        def saveListener():
            FILE_TYPES = [('Postscript File','*.ps'), ('Any File','*')]
            f = tkFileDialog.asksaveasfilename(defaultextension='.ps',
                filetypes=FILE_TYPES)
            self._canvas.postscript(file=f, x=0, y=0,
                height=self._height, width=self._width)

        # Create a menu containing a 'Save' menu item.
        self._saveMenu = Tkinter.Menu()
        self._saveMenu.add_command(label='Save...',
            command=saveListener)
        self._saveMenu['tearoff'] = 0
        self._menubar = Tkinter.Menu()
        self._menubar.add_cascade(label='File', menu=self._saveMenu)
        self._toplevel['menu'] = self._menubar

    #-------------------------------------------------------------------

    # Helper methods that scale from user coordinates to canvas
    # coordinates and back.

    def _scaleX(self, x):
        return self._width * (x - self._xmin) / \
            (self._xmax - self._xmin)

    def _scaleY(self, y):
        return self._height * (self._ymax - y) / \
            (self._ymax - self._ymin)

    def _factorX(self, w):
        return w * self._width / abs(self._xmax - self._xmin)

    def _factorY(self, h):
        return h * self._height / abs(self._ymax - self._ymin)

    #-------------------------------------------------------------------

    def setCanvasSize(self, w=_DEFAULT_SIZE, h=_DEFAULT_SIZE):
        """
        Set the size of self's canvas to w by h pixels.
        """
        if (w < 1) or (h < 1):
            raise Exception('w and h must be positive')
        self._width = w
        self._height = h
        self._canvas.config(width=self._width, height=self._height)

    def setXscale(self, min=_DEFAULT_XMIN, max=_DEFAULT_XMAX):
        """
        Set the x-scale of self's canvas such that the minimum x value
        is min and the maximum x value is max.  Add a 10% border.
        """
        size = max - min
        self._xmin = min - _BORDER * size
        self._xmax = max + _BORDER * size

    def setYscale(self, min=_DEFAULT_YMIN, max=_DEFAULT_YMAX):
        """
        Set the y-scale of self's canvas such that the minimum y value
        is min and the maximum y value is max.  Add a 10% border.
        """
        size = max - min
        self._ymin = min - _BORDER * size
        self._ymax = max + _BORDER * size

    def setPenRadius(self, r=_DEFAULT_PEN_RADIUS):
        """
        Set self's pen radius to r.
        """
        if r < 0:
            raise Exception('Arg to setPenRadius() must be non-neg')
        self._penRadius = r * _DEFAULT_SIZE

    def setPenColor(self, c=_DEFAULT_PEN_COLOR):
        """
        Set self's pen color to c, where c is an object of class
        color.Color.
        """
        self._penColor = c

    #-------------------------------------------------------------------

    def _pixel(self, x, y):
        """
        Draw in self's canvas a pixel at (x, y).
        """
        xs = self._scaleX(x)
        ys = self._scaleY(y)
        try:
            self._canvas.create_oval(xs, ys, xs, ys,
                fill=str(self._penColor), outline=str(self._penColor))
        except Tkinter.TclError:
            sys.exit()
        self._draw()

    def point(self, x, y):
        """
        Draw in self's canvas a point at (x, y).
        """
        r = self._penRadius
        if r <= 1:
            self._pixel(x, y)
        else:
            xs = self._scaleX(x)
            ys = self._scaleY(y)
            try:
                self._canvas.create_oval(xs-r/2, ys-r/2, xs+r/2, ys+r/2,
                    fill=str(self._penColor),
                    outline=str(self._penColor))
            except Tkinter.TclError:
                sys.exit()
            self._draw()

    def line(self, x0, y0, x1, y1):
        """
        Draw in self's canvas a line from (x0, y0) to (x1, y1).
        """
        x0s = self._scaleX(x0)
        y0s = self._scaleY(y0)
        x1s = self._scaleX(x1)
        y1s = self._scaleY(y1)
        try:
            self._canvas.create_line(x0s, y0s, x1s, y1s,
                width=self._penRadius, fill=str(self._penColor))
        except Tkinter.TclError:
            sys.exit()
        self._draw()

    def filledCircle(self, x, y, r):
        """
        Draw in self's canvas a filled circle of radius r centered on
        (x, y).
        """
        ws = self._factorX(2*r)
        hs = self._factorY(2*r)
        if (ws <= 1) and (hs <= 1):
            self._pixel(x, y)
        else:
            xs = self._scaleX(x)
            ys = self._scaleY(y)
            try:
                self._canvas.create_oval(xs-ws/2, ys-hs/2, xs+ws/2,
                    ys+hs/2, fill=str(self._penColor),
                    outline=str(self._penColor))
            except Tkinter.TclError:
                sys.exit()
            self._draw()

    def filledSquare(self, x, y, r):
        """
        Draw in self's canvas a filled square whose sides are of length
        2r, centered on (x, y).
        """
        ws = self._factorX(2*r)
        hs = self._factorY(2*r)
        if (ws <= 1) and (hs <= 1):
            self._pixel(x, y)
        else:
            xs = self._scaleX(x)
            ys = self._scaleY(y)
            try:
                self._canvas.create_rectangle(xs-ws/2, ys-hs/2,
                    xs+ws/2, ys+hs/2, fill=str(self._penColor),
                    outline=str(self._penColor))
            except Tkinter.TclError:
                sys.exit()
            self._draw()

    def filledRectangle(self, x, y, w, h):
        """
        Draw in self's canvas a filled rectangle of width w and height
        h, centered on (x, y).
        """
        ws = self._factorX(2*w)
        hs = self._factorY(2*h)
        if (ws <= 1) and (hs <= 1):
            self._pixel(x, y)
        else:
            xs = self._scaleX(x)
            ys = self._scaleY(y)
            try:
                self._canvas.create_rectangle(xs-ws/2, ys-hs/2,
                    xs+ws/2, ys+hs/2, fill=str(self._penColor),
                    outline=str(self._penColor))
            except Tkinter.TclError:
                sys.exit()
            self._draw()

    def clear(self):
        """
        Clear self's canvas.
        """
        try:
            self._canvas.delete(Tkinter.ALL)
            self._draw()
        except Tkinter.TclError:
            sys.exit()

    #-------------------------------------------------------------------

    def _draw(self):
        """
        Update self's canvas if deferDraw is False.
        """
        if not self._deferDraw:
            try:
                self._toplevel.update()
            except Tkinter.TclError:
                sys.exit()

    def show(self, t=None):
        """
        Update self's canvas.  If t is given, defer subsequent updates
        for t milliseconds.
        """
        self._deferDraw = False
        self._draw()
        if t != None:
            time.sleep(float(t) / 1000.0)
            self._deferDraw = True
