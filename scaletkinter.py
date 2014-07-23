
#-----------------------------------------------------------------------
# scale.py
#-----------------------------------------------------------------------

import sys
import picturetkinter as picture

#-----------------------------------------------------------------------

# Accept the name of a GIF or JPG image file, an integer width, and 
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

    source.show()
    target.show()
    picture.wait()

if __name__ == '__main__':
    main(sys.argv)