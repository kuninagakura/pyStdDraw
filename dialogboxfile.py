#!/usr/bin/env python

import sys
import Tkinter
import tkFileDialog

def main():
    root = Tkinter.Tk()
    root.withdraw()
    reply = tkFileDialog.asksaveasfilename(initialdir='.')
    sys.stdout.write(reply)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
