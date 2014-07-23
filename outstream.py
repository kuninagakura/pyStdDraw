"""
outstream.py

The outstream module defines the OutStream class.
"""

#-----------------------------------------------------------------------

class OutStream:

    """
    An OutStream object wraps around a text file or sys.stdout, and
    supports writing to that stream.
    """

    #-------------------------------------------------------------------

    def __init__(self, file=None):
        """
        Construct 'self' to wrap around a stream. If 'file' (a file name)
        is provided, then the stream is a file of that name.  Otherwise
        the stream is sys.stdout.
        """
        if file == None:
            self._stream = sys.stdout
        else:
            self._stream = open(file, 'w')

    #-------------------------------------------------------------------

    def writeln(self, x=''):
        """
        Write x and an end-of-line mark to the stream wrapped by 'self'.
        """
        self._stream.write(str(x) + '\n')
        self._stream.flush()

    #-------------------------------------------------------------------

    def write(self, x=''):
        """
        Write x to the stream wrapped by 'self'.
        """
        self._stream.write(str(x))
        self._stream.flush()

    #-------------------------------------------------------------------

    def writef(self, fmt, *args):
        """
        Write each element of 'args' to the stream wrapped by 'self'.
        Use the format specified by string 'fmt'.
        """
        self._stream.write(fmt % args)
        self._stream.flush()
