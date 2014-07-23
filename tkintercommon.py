#=======================================================================
# tkintercommon.py
#=======================================================================

import sys
if sys.hexversion < 0x03000000:
    import Tkinter
else:
    import tkinter as Tkinter

#-----------------------------------------------------------------------

# Start the Tcl interpreter and Tk, and create the root Toplevel object.
root = Tkinter.Tk()

# Has the root Toplevel object been used?
rootUsed = False

#-----------------------------------------------------------------------

# Delay process termination by starting a Tkinter main loop.

def wait():
    root.mainloop()
