
"""
stdio.py

The stdio module supports reading from sys.stdin and writing to
sys.stdout.

Note:  Usually it's a bad idea to mix these two sets of reading
functions:
-- isEmpty(), readInt(), readFloat(), readBool(), readString()
-- hasNextLine(), readLine(), readAll()
Usually it's better to use one set or the other exclusively.
"""

import sys
import re

#=======================================================================
# Writing functions
#=======================================================================

def writeln(x=''):
    """
    Write x and an end-of-line mark to sys.stdout.
    """
    sys.stdout.write(str(x) + '\n')
    sys.stdout.flush()

#-----------------------------------------------------------------------

def write(x=''):
    """
    Write x to sys.stdout.
    """
    sys.stdout.write(str(x))
    sys.stdout.flush()

#-----------------------------------------------------------------------

def writef(fmt, *args):
    """
    Write each element of 'args' to sys.stdout.  Use the format
    specified by string 'fmt'.
    """

    sys.stdout.write(fmt % args)
    sys.stdout.flush()

#=======================================================================
# Reading functions
#=======================================================================

_buffer = ''

#-----------------------------------------------------------------------

def _readRegExp(regExp):
    """
    Discard leading white space characters from sys.stdin. Then read
    from sys.stdin and return a string matching regular expression
    'regExp'.  Raise an EOFError if no non-whitespace characters remain
    in sys.stdin.  Raise a ValueError if the next characters to be read
    from sys.stdin do not match 'regExp'.
    """
    global _buffer
    if isEmpty():
        raise EOFError()
    compiledRegExp = re.compile(r'^\s*' + regExp)
    match = compiledRegExp.search(_buffer)
    if match == None:
        raise ValueError()
    s = match.group()
    _buffer = _buffer[match.end():]
    return s.lstrip()

#-----------------------------------------------------------------------

def isEmpty():
    """
    Return True iff no non-whitespace characters remain in sys.stdin.
    """
    global _buffer
    while _buffer.strip() == '':
        line = sys.stdin.readline()
        if line == '':
            return True
        _buffer += line
    return False

#-----------------------------------------------------------------------

def readInt():
    """
    Discard leading white space characters from sys.stdin. Then read
    from sys.stdin a sequence of characters comprising an integer.
    Convert the sequence of characters to an integer, and return the
    integer.  Raise an EOFError if no non-whitespace characters remain
    in sys.stdin. Raise a ValueError if the next characters to be read
    from sys.stdin cannot comprise an integer.
    """
    s = _readRegExp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
    radix = 10
    strLength = len(s)
    if (strLength >= 1) and (s[0:1] == '0'): radix = 8
    if (strLength >= 2) and (s[0:2] == '-0'): radix = 8
    if (strLength >= 2) and (s[0:2] == '0x'): radix = 16
    if (strLength >= 2) and (s[0:2] == '0X'): radix = 16
    if (strLength >= 3) and (s[0:3] == '-0x'): radix = 16
    if (strLength >= 3) and (s[0:3] == '-0X'): radix = 16
    return int(s, radix)

#-----------------------------------------------------------------------

def readFloat():
    """
    Discard leading white space characters from sys.stdin. Then read
    from sys.stdin a sequence of characters comprising a float.
    Convert the sequence of characters to a float, and return the
    float.  Raise an EOFError if no non-whitespace characters remain
    in sys.stdin. Raise a ValueError if the next characters to be read
    from sys.stdin cannot comprise a float.
    """
    s = _readRegExp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    return float(s)

#-----------------------------------------------------------------------

def readBool():
    """
    Discard leading white space characters from sys.stdin. Then read
    from sys.stdin a sequence of characters comprising a bool.
    Convert the sequence of characters to a bool, and return the
    bool.  Raise an EOFError if no non-whitespace characters remain
    in sys.stdin. Raise a ValueError if the next characters to be read
    from sys.stdin cannot comprise a bool.

    These character sequences can comprise a bool:
    -- True
    -- False
    -- 1 (means true)
    -- 0 (means false)
    """
    s = _readRegExp(r'(True)|(False)|1|0')
    if (s == 'True') or (s == '1'):
        return True
    return False

#-----------------------------------------------------------------------

def readString():
    """
    Discard leading white space characters from sys.stdin. Then read
    from sys.stdin a sequence of characters comprising a string, and
    return the string. Raise an EOFError if no non-whitespace
    characters remain in sys.stdin.
    """
    s = _readRegExp(r'\S+')
    return s

def hasNextLine():
    """
    Return True iff sys.stdin has a next line.
    """
    global _buffer
    if _buffer != '':
        return True
    else:
        _buffer = sys.stdin.readline()
        if _buffer == '':
            return False
        return True

#-----------------------------------------------------------------------

def readLine():
    """
    Read and return as a string the next line of sys.stdin.
    Raise an EOFError is there is no next line.
    """
    global _buffer
    if not hasNextLine():
        raise EOFError()
    s = _buffer
    _buffer = ''
    return s.rstrip('\n')

#-----------------------------------------------------------------------

def readAll():
    """
    Read and return as a string all remaining lines of sys.stdin.
    """
    global _buffer
    s = _buffer
    _buffer = ''
    for line in sys.stdin:
        s += line
    return s

#=======================================================================
# For Testing
#=======================================================================

def _testWrite():
    writeln()
    writeln('string')
    writeln(123456)
    writeln(123.456)
    writeln(True)
    write()
    write('string')
    write(123456)
    write(123.456)
    write(True)
    writeln()
    writef('<%s> <%8d> <%14.8f>\n', 'string', 123456, 123.456)
    writef('formatstring\n')

def _testReadInt():
    while not isEmpty():
        i = readInt()
        writeln('Int: ' + str(i))

def _testReadFloat():
    while not isEmpty():
        f = readFloat()
        writeln('Float: ' + str(f))

def _testReadBool():
    while not isEmpty():
        b = readBool()
        writeln('Bool: ' + str(b))

def _testReadString():
    while not isEmpty():
        s = readString()
        writeln('String: ' + s)

def _testReadLine():
    while hasNextLine():
        line = readLine()
        write('Line: ' + line)

def _testReadAll():
    s = readAll()
    write(s)

def main():
    """
    For testing.
    """
    _testWrite()

    write('Integer: ')
    i = readInt()
    writeln('Integer: ' + str(i))

    write('Float: ')
    f = readFloat()
    writeln('Float: ' + str(f))

    write('Bool: ')
    b = readBool()
    writeln('Bool: ' + str(b))

    write('String: ')
    s = readString()
    writeln('String: ' + s)

    #_testReadInt()
    #_testReadFloat()
    #_testReadBool()
    #_testReadString()
    #_testReadLine()
    #_testReadAll()

if __name__ == '__main__':
    main()
