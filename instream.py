
"""
instream.py

The instream module defines the InStream class.
"""

#-----------------------------------------------------------------------

import sys
if sys.hexversion < 0x03000000:
    import urllib
else:
    import urllib.request as urllib
import re

#-----------------------------------------------------------------------

class InStream:

    """
    An InStream object wraps around a text file or sys.stdin, and
    supports reading from that stream.

    Note:  Usually it's a bad idea to mix these two sets of methods:
    -- isEmpty(), readInt(), readFloat(), readBool(), readString()
    -- hasNextLine(), readLine(), readAll()
    Usually it's better to use one set or the other exclusively.
    """

    #-------------------------------------------------------------------

    def __init__(self, fileOrUrl=None):
        """
        Construct 'self' to wrap around a stream. The stream can be
        a file whose name is given as 'fileOrUrl', a resource whose URL
        is given as 'fileOrUrl', or sys.stdin by default.
        """

        self._buffer = ''
        self._stream = None

        if fileOrUrl == None:
            self._stream = sys.stdin
            return

        # Try to open a file, then a URL.
        try:
            self._stream = open(fileOrUrl, mode='r')
        except IOError:
            try:
                self._stream = urllib.urlopen(fileOrUrl)
            except IOError:
                raise Exception('No such file or URL')

    #-------------------------------------------------------------------

    def _readRegExp(self, regExp):
        """
        Discard leading white space characters from the stream wrapped
        by 'self'.  Then read from the stream and return a string
        matching regular expression 'regExp'.  Raise an EOFError if no
        non-whitespace characters remain in the stream. Raise a
        ValueError if the next characters to be read from the stream
        do not match 'regExp'.
        """
        if self.isEmpty():
            raise EOFError()
        compiledRegExp = re.compile(r'^\s*' + regExp)
        match = compiledRegExp.search(self._buffer)
        if match == None:
            raise ValueError()
        s = match.group()
        self._buffer = self._buffer[match.end():]
        return s.lstrip()

    #-------------------------------------------------------------------

    def isEmpty(self):
        """
        Return True iff no non-whitespace characters remain in the
        stream wrapped by 'self'.
        """
        while self._buffer.strip() == '':
            line = str(self._stream.readline())
            if line == '':
                return True
            self._buffer += line
        return False

    #-------------------------------------------------------------------

    def readInt(self):
        """
        Discard leading white space characters from the stream wrapped
        by 'self'.  Then read from the stream a sequence of characters
        comprising an integer.  Convert the sequence of characters to an
        integer, and return the integer.  Raise an EOFError if no
        non-whitespace characters remain in the stream.  Raise a
        ValueError if the next characters to be read from the stream
        cannot comprise an integer.
        """
        s = self._readRegExp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
        radix = 10
        strLength = len(s)
        if (strLength >= 1) and (s[0:1] == '0'): radix = 8
        if (strLength >= 2) and (s[0:2] == '-0'): radix = 8
        if (strLength >= 2) and (s[0:2] == '0x'): radix = 16
        if (strLength >= 2) and (s[0:2] == '0X'): radix = 16
        if (strLength >= 3) and (s[0:3] == '-0x'): radix = 16
        if (strLength >= 3) and (s[0:3] == '-0X'): radix = 16
        return int(s, radix)

    #-------------------------------------------------------------------

    def readFloat(self):
        """
        Discard leading white space characters from the stream wrapped
        by 'self'.  Then read from the stream a sequence of characters
        comprising a float.  Convert the sequence of characters to an
        float, and return the float.  Raise an EOFError if no
        non-whitespace characters remain in the stream.  Raise a
        ValueError if the next characters to be read from the stream
        cannot comprise a float.
        """
        s = self._readRegExp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
        return float(s)

    #-------------------------------------------------------------------

    def readBool(self):
        """
        Discard leading white space characters from the stream wrapped
        by 'self'.  Then read from the stream a sequence of characters
        comprising a bool.  Convert the sequence of characters to an
        bool, and return the bool.  Raise an EOFError if no
        non-whitespace characters remain in the stream.  Raise a
        ValueError if the next characters to be read from the stream
        cannot comprise an bool.
        """
        s = self._readRegExp(r'(True)|(False)|1|0')
        if (s == 'True') or (s == '1'):
            return True
        return False

    #-------------------------------------------------------------------

    def readString(self):
        """
        Discard leading white space characters from the stream wrapped
        by 'self'.  Then read from the stream a sequence of characters
        comprising a string, and return the string. Raise an EOFError
        if no non-whitespace characters remain in the stream.
        """
        s = self._readRegExp(r'\S+')
        return s

    def hasNextLine(self):
        """
        Return True iff the stream wrapped by 'self' has a next line.
        """
        if self._buffer != '':
            return True
        else:
            self._buffer = str(self._stream.readline())
            if self._buffer == '':
                return False
            return True

    #-------------------------------------------------------------------

    def readLine(self):
        """
        Read and return as a string the next line of the stream wrapped
        by 'self'.  Raise an EOFError is there is no next line.
        """
        if not self.hasNextLine():
            raise EOFError()
        s = self._buffer
        self._buffer = ''
        return s.rstrip('\n')

    #-------------------------------------------------------------------

    def readAll(self):
        """
        Read and return as a string all remaining lines of the stream
        wrapped by 'self'.
        """
        s = self._buffer
        self._buffer = ''
        for line in self._stream:
            s += str(line)
        return s
