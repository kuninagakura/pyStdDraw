#-----------------------------------------------------------------------
# scale.py
#-----------------------------------------------------------------------

import stddraw
import sys
import picture

#-----------------------------------------------------------------------

# Accept the name of a JPG or PNG image file, an integer width, and
# an integer height as command line arguments. Read an image from the
# file, display the image, and also display the image scaled to the
# given width and height.

def main(argv):

    fileName = argv[1]
    w = int(argv[2])
    h = int(argv[3])

    source = picture.Picture()
    source.load(fileName)

    target = picture.Picture(w, h)

    for ti in range(w):
        for tj in range(h):
            si = ti * source.width() // w
            sj = tj * source.height() // h
            target.set(ti, tj, source.get(si, sj))

    maxHeight = max(source.height(), target.height())

    stddraw.createWindow(source.width() + target.width(), maxHeight)
    stddraw.setXscale(0, source.width() + target.width())
    stddraw.setYscale(0, maxHeight)

    stddraw.picture(source, source.width()/2, maxHeight/2)
    stddraw.picture(target, source.width() + target.width()/2,
        maxHeight/2)

    stddraw.show()
    stddraw.wait()

if __name__ == '__main__':
    main(sys.argv)
