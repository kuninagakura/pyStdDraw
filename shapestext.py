#-----------------------------------------------------------------------
# shapestext.py
#-----------------------------------------------------------------------

import stddraw

# Draw some shapes and some text.
stddraw.createWindow()
stddraw.square(.2, .8, .1)

stddraw.filledSquare(.8, .8, .2)

stddraw.circle(.8, .2, .2)

xd = [.1, .2, .3, .2]
yd = [.2, .3, .2, .1]
stddraw.filledPolygon(xd, yd)

stddraw.setFontFamily('Times')
stddraw.setFontSize(40)
stddraw.text(.2, .5, 'black')

stddraw.setPenColor(stddraw.WHITE)
stddraw.setFontFamily('Courier')
stddraw.setFontSize(30)
stddraw.text(.8, .8, 'white')

stddraw.show()
stddraw.wait()
