"""
stddraw.py

The stddraw module defines functions that allow the user to create a
drawing.  A drawing is rendered on a canvas, which appears within a
window.  As a convenience, the module also imports the commonly used
Color objects defined in the color module.
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

_BORDER = 0.05
_DEFAULT_XMIN = 0.0
_DEFAULT_XMAX = 1.0
_DEFAULT_YMIN = 0.0
_DEFAULT_YMAX = 1.0
_DEFAULT_SIZE = 512
_DEFAULT_PEN_RADIUS = .002
_DEFAULT_PEN_COLOR = BLACK
_DEFAULT_FONT_FAMILY = 'Helvetica'
_DEFAULT_FONT_SIZE = 12

_xmin = None
_ymin = None
_xmax = None
_ymax = None

_width = _DEFAULT_SIZE
_height = _DEFAULT_SIZE
_penRadius = None
_penColor = _DEFAULT_PEN_COLOR
_fontFamily = _DEFAULT_FONT_FAMILY
_font_size = _DEFAULT_FONT_SIZE

# Should drawing be deferred?
_deferDraw = False

#-----------------------------------------------------------------------

# Helper functions that scale from user coordinates to canvas
# coordinates and back.

def _scaleX(x):
    return _width * (x - _xmin) / (_xmax - _xmin)

def _scaleY(y):
    return _height * (_ymax - y) / (_ymax - _ymin)

def _factorX(w):
    return w * _width / abs(_xmax - _xmin)

def _factorY(h):
    return h * _height / abs(_ymax - _ymin)

#-----------------------------------------------------------------------

def setCanvasSize(w=_DEFAULT_SIZE, h=_DEFAULT_SIZE):
    """
    Set the canvas size to w by h pixels.
    """
    global _width
    global _height
    if (w < 1) or (h < 1):
        raise Exception('w and h must be positive')
    _width = w
    _height = h
    _canvas.config(width=_width, height=_height)

def setXscale(min=_DEFAULT_XMIN, max=_DEFAULT_XMAX):
    """
    Set the x-scale of the canvas such that the minimum x value is
    min and the maximum x value is max.  Add a 10% border.
    """
    global _xmin
    global _xmax
    size = max - min
    _xmin = min - _BORDER * size
    _xmax = max + _BORDER * size

def setYscale(min=_DEFAULT_YMIN, max=_DEFAULT_YMAX):
    """
    Set the y-scale of the canvas such that the minimum y value is
    min and the maximum y value is max.  Add a 10% border.
    """
    global _ymin
    global _ymax
    size = max - min
    _ymin = min - _BORDER * size
    _ymax = max + _BORDER * size

def setPenRadius(r=_DEFAULT_PEN_RADIUS):
    """
    Set the pen radius to r.
    """
    global _penRadius
    if r < 0:
        raise Exception('Argument to setPenRadius() must be non-neg')
    _penRadius = r * _DEFAULT_SIZE

def setPenColor(c=_DEFAULT_PEN_COLOR):
    """
    Set the pen color to c, where c is an object of class color.Color.
    """
    global _penColor
    _penColor = c

def setFontFamily(f=_DEFAULT_FONT_FAMILY):
    """
    Set the font family to f (e.g. 'Helvetica' or 'Courier').
    """
    global _fontFamily
    _fontFamily = f

def setFontSize(s=_DEFAULT_FONT_SIZE):
    """
    Set the font size to s (e.g. 12 or 16).
    """
    global _fontSize
    _fontSize = s


#-----------------------------------------------------------------------

def _pixel(x, y):
    """
    Draw in the canvas a pixel at (x, y).
    """
    xs = _scaleX(x)
    ys = _scaleY(y)
    try:
        _canvas.create_oval(xs, ys, xs, ys,
            fill=str(_penColor), outline=str(_penColor))
    except Tkinter.TclError:
        sys.exit()
    _draw()

def point(x, y):
    """
    Draw in the canvas a point at (x, y).
    """
    r = _penRadius
    if r <= 1:
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_oval(xs-r/2, ys-r/2, xs+r/2, ys+r/2,
                fill=str(_penColor), outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()

def line(x0, y0, x1, y1):
    """
    Draw in the canvas a line from (x0, y0) to (x1, y1).
    """
    x0s = _scaleX(x0)
    y0s = _scaleY(y0)
    x1s = _scaleX(x1)
    y1s = _scaleY(y1)
    try:
        _canvas.create_line(x0s, y0s, x1s, y1s,
            width=_penRadius, fill=str(_penColor))
    except Tkinter.TclError:
        sys.exit()
    _draw()

def circle(x, y, r):
    """
    Draw in the canvas a circle of radius r centered on (x, y).
    """
    ws = _factorX(2*r)
    hs = _factorY(2*r)
    if (ws <= 1) and (hs <= 1):
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_oval(xs-ws/2, ys-hs/2, xs+ws/2, ys+hs/2,
                outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()


def filledCircle(x, y, r):
    """
    Draw in the canvas a filled circle of radius r centered on (x, y).
    """
    ws = _factorX(2*r)
    hs = _factorY(2*r)
    if (ws <= 1) and (hs <= 1):
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_oval(xs-ws/2, ys-hs/2, xs+ws/2, ys+hs/2,
                fill=str(_penColor), outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()

def square(x, y, r):
    """
    Draw in the canvas a square whose sides are of length 2r,
    centered on (x, y).
    """
    ws = _factorX(2*r)
    hs = _factorY(2*r)
    if (ws <= 1) and (hs <= 1):
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_rectangle(xs-ws/2, ys-hs/2, xs+ws/2, ys+hs/2,
                outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()

def filledSquare(x, y, r):
    """
    Draw in the canvas a filled square whose sides are of length 2r,
    centered on (x, y).
    """
    ws = _factorX(2*r)
    hs = _factorY(2*r)
    if (ws <= 1) and (hs <= 1):
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_rectangle(xs-ws/2, ys-hs/2, xs+ws/2, ys+hs/2,
                fill=str(_penColor), outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()

def rectangle(x, y, w, h):
    """
    Draw in the canvas a rectangle of width w and height h,
    centered on (x, y).
    """
    ws = _factorX(2*w)
    hs = _factorY(2*h)
    if (ws <= 1) and (hs <= 1):
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_rectangle(xs-ws/2, ys-hs/2, xs+ws/2, ys+hs/2,
                outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()

def filledRectangle(x, y, w, h):
    """
    Draw in the canvas a filled rectangle of width w and height h,
    centered on (x, y).
    """
    ws = _factorX(2*w)
    hs = _factorY(2*h)
    if (ws <= 1) and (hs <= 1):
        _pixel(x, y)
    else:
        xs = _scaleX(x)
        ys = _scaleY(y)
        try:
            _canvas.create_rectangle(xs-ws/2, ys-hs/2, xs+ws/2, ys+hs/2,
                fill=str(_penColor), outline=str(_penColor))
        except Tkinter.TclError:
            sys.exit()
        _draw()

def polygon(x, y):
    """
    Draw in the canvas a polygon with coordinates (x[i], y[i]).
    """
    xScaled = []
    for xi in x:
        xScaled += [_scaleX(xi)]

    yScaled = []
    for yi in y:
        yScaled += [_scaleY(yi)]

    points = []
    for i in range(len(x)):
        points += [(xScaled[i], yScaled[i])]
    points += [(xScaled[0], yScaled[0])]

    try:
        _canvas.create_line(*points,
            width=_penRadius)
    except Tkinter.TclError:
        sys.exit()
    _draw()

def filledPolygon(x, y):
    """
    Draw in the canvas a filled polygon with coordinates (x[i], y[i]).
    """
    xScaled = []
    for xi in x:
        xScaled += [_scaleX(xi)]

    yScaled = []
    for yi in y:
        yScaled += [_scaleY(yi)]

    points = []
    for i in range(len(x)):
        points += [(xScaled[i], yScaled[i])]

    try:
        _canvas.create_polygon(*points,
            width=_penRadius, fill=str(_penColor))
    except Tkinter.TclError:
        sys.exit()
    _draw()

def text(x, y, s):
    """
    Draw string s in the canvas centered at (x, y).
    """
    xs = _scaleX(x)
    ys = _scaleY(y)
    try:
        _canvas.create_text(xs, ys, text=s, \
            font=(_fontFamily, _fontSize), fill=str(_penColor))
    except Tkinter.TclError:
        sys.exit()
    _draw()

def clear():
    """
    Clear the canvas.
    """
    try:
        _canvas.delete(Tkinter.ALL)
        _draw()
    except Tkinter.TclError:
        sys.exit()

#-----------------------------------------------------------------------

def _draw():
    """
    Update the canvas if deferDraw is False.
    """
    if not _deferDraw:
        try:
            _toplevel.update()
        except Tkinter.TclError:
            sys.exit()

def show(t=None):
    """
    Update the canvas.  If t is given, defer subsequent updates
    for t milliseconds.
    """
    global _deferDraw
    _deferDraw = False
    _draw()
    if t != None:
        time.sleep(float(t) / 1000.0)
        _deferDraw = True

def wait():
    """
    Wait for the user to close this application's primary window.
    """
    tkintercommon.wait()

#-----------------------------------------------------------------------

_keysTyped = []

def hasNextKeyTyped():
    """
    Return True iff queue of keys the user typed is not empty.
    """
    global _keysTyped
    return _keysTyped != []

def nextKeyTyped():
    """
    Remove the first key from the queue of keys that the the user typed,
    and return that key.
    """
    global _keysTyped
    return _keysTyped.pop()

def _keyTyped(event):
    """
    Add the key that the user typed to the queue.
    """
    global _keysTyped
    _keysTyped = [event.char] + _keysTyped  # a little slow

#-----------------------------------------------------------------------

setXscale()
setYscale()
setPenRadius()

# The drawing is rendered via a Toplevel object.
# Use the root Toplevel object if it's available. Otherwise
# create and use a new Toplevel object.
if not tkintercommon.rootUsed:
    _toplevel = tkintercommon.root
    tkintercommon.rootUsed = True
else:
    _toplevel = Tkinter.toplevel()
_toplevel.title('Stddraw Window')

# Create a Canvas object and place it in the Toplevel object,
_canvas = Tkinter.Canvas(_toplevel, width=_DEFAULT_SIZE,
    height=_DEFAULT_SIZE)
_canvas.pack()

# Register keyTyped() as the handler for <Key> events on the
# Toplevel object.
_toplevel.bind('<Key>', _keyTyped)

# Define a listener for the 'Save' menu item.
def _saveListener():
    FILE_TYPES = [('Postscript File','*.ps'), ('Any File','*')]
    f = tkFileDialog.asksaveasfilename(defaultextension='.ps',
        filetypes=FILE_TYPES)
    _canvas.postscript(file=f, x=0, y=0, height=_height,
        width=_width)

# Create a menu containing a Save menu item.
_saveMenu = Tkinter.Menu()
_saveMenu.add_command(label='Save...', command=_saveListener)
_saveMenu['tearoff'] = 0
_menubar = Tkinter.Menu()
_menubar.add_cascade(label='File', menu=_saveMenu)
_toplevel['menu'] = _menubar
