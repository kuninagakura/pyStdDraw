#!/usr/bin/env python

import stddraw

def main():
	stddraw.createWindow()
	import Tkinter as tk
	import tkFileDialog
	root = tk.Tk()
	root.withdraw()
	reply = tkFileDialog.asksaveasfilename(initialdir='.')
	print reply

    # Other functions:
    #     askopenfilename()
    #     askdirectory()
    #     askopenfilenames()

if __name__ == '__main__':
    main()