#!/usr/bin/env python

import Tkinter
import tkMessageBox

def main():
    root = Tkinter.Tk()
    root.withdraw()
    tkMessageBox.showinfo(title='File Save Confirmation',
        message='The drawing was saved to the file.')

if __name__ == '__main__':
    main()
