#!/usr/bin/env python

import Tkinter
import tkMessageBox

def main():
    root = Tkinter.Tk()
    root.withdraw()
    tkMessageBox.showerror(title='File Save Error',
        message='Error: File name must end with .jpg or .png.')

if __name__ == '__main__':
    main()
