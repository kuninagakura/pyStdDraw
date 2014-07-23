import sys
if sys.hexversion < 0x03000000:
    import Tkinter
else:
    import tkinter as Tkinter
#import tkintercommon
import tkSnack
import sys
import stdio
import math
import time

# Lots of help from this web page:
# http://www.daniweb.com/software-development/python/code/216655

SAMPLE_RATE = 44100

def setVolume(volume=50):
    if volume > 100:
        volume = 100
    if volume < 0:
        volume = 0
    tkSnack.audio.play_gain(volume)

def playFile(file):
    notes = read(file)
    playNotes(notes)

    # Doesn't work on Mac:
    #sound = tkSnack.Sound()
    #sound.read(file)
    #sound.play(blocking=1)
    #sound.stop()

blocked = False

def unblock():
    global blocked
    global root
    print 'In unblock'
    #time.sleep(.01)
    blocked = False

def playNote(freq, duration):
    global mySound
    mySound.stop()
    mySound.flush()
    #mySound = tkSnack.Sound()
    filt = tkSnack.Filter('generator', freq, 30000, 0.0,
        'sine', int(11500*duration))
    #mySound.stop()
    mySound.play(filter=filt, blocking=0)
    root.update()

oldLength = SAMPLE_RATE

def wait():
    global blocked
    print 'In wait'
    print 'blocked at beg of wait:', blocked
    while blocked:
        #pass
        time.sleep(.01)

def unblock():
    global blocked
    print 'In unblock'
    blocked = False
    print 'blocked at end of unblock:', blocked

_startTime = time.clock()
_length = 0
_firstTime = True

def playNotes(notes):
    print 'In playNotes'
    global root
    global blocked
    #global oldLength
    #global globalSound
    #global blocked
    #while blocked:
    #    print 'blocked'
    #blocked = True

    sound = tkSnack.Sound(frequency=SAMPLE_RATE, buffersize=0)
    length = len(notes)
    sound.length(length)
    for i in range(length):
        sound.sample(i, int(notes[i] * 30000))

    #oldLength = globalSound.length()
    #globalSound.concatenate(sound)
    #newLength = globalSound.length()
    #if newLength - oldLength > 1000:
    #globalSound.play(blocking=0, start=oldLength, end=-1,
    #    command=unblock())
    #root.update()
    #time.sleep(.1)

    #if globalSound.length() >= 4096:
    #    globalSound.play(blocking=0, start=)
    #    root.update()
        #globalSound.flush()
    #while block:
    #    print 'blocked'
    #block = True
    #sound.play(blocking=0, command=unblock())
    #newDelay = sound.length(unit='SECONDS')
    #print 'Delay:', newDelay
    #length = sound.length(unit='SAMPLES')
    #print 'Length:', length
    #print int(2000.0*oldLength/SAMPLE_RATE)
    #sound.play(blocking=1, starttime=0)
    #sound.play(blocking=0)

    #root.update()
    #wait()
    #blocked = True
    #sound.play(blocking=0, command=unblock())

    global _startTime
    global _length
    global _firstTime
    #print 'Starttime:', _startTime
    #print 'Currenttime:', time.time()
    #print 'Length:', _length
    #print 'firsttime:', _firstTime
    if _firstTime:
        _firstTime = False
    else:
        #print 'here'
        while (time.time() - _startTime) < _length:
            #print 'sleeping'
            pass
            #time.sleep(1)
    sound.play(blocking=0)
    _startTime = time.time()
    #_length = sound.length(unit='SAMPLES')
    #print 'initiallength:', _length
    _length = float(length) / 44100.0
    root.update()

    #oldLength = length
    #delay = newDelay
    #time.sleep(.01)
    #sound.stop()

def save(file, notes):
    sound = tkSnack.Sound(frequency=SAMPLE_RATE)
    length = len(notes)
    sound.length(length)
    for i in range(length):
        sound.sample(i, int(notes[i] * 30000))
    sound.write(file, fileformat='WAV')

def read(file):
    sound = tkSnack.Sound()
    sound.read(file, fileformat='WAV')
    sound.convert(frequency=SAMPLE_RATE)
    notes = []
    for i in range(sound.length()):
        notes.append(sound.sample(i)/30000.0)
    return notes

#-----------------------------------------------------------------------


# For testing:

def playTune():
    sps = SAMPLE_RATE
    while not stdio.isEmpty():
        pitch = stdio.readInt()
        duration = stdio.readFloat()
        hz = 440 * math.pow(2, pitch / 12.0)
        N = int(sps * duration)
        notes = []
        for i in range(N+1):
            notes.append(math.sin(2*math.pi * i * hz / sps))
        #stdio.writeln('Playing')
        playNotes(notes)

def playTune2():
    notes = []
    #while not stdio.isEmpty():
    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = 440 * math.pow(2, pitch / 12.0)
    playNote(hz, 1)

root = Tkinter.Tk()
tkSnack.initializeSnack(root)
mySound = tkSnack.Sound(frequency=SAMPLE_RATE)

#pressed = False

def keyPressFunc(event):
    print 'in keyPressFunc'
    #mySound.stop()
    #time.sleep(1)
    #global pressed
    #if pressed:
    #    return
    #pressed = True
    if event.keysym == 'a':
        playNote(440.0, .25)
    if event.keysym == 'c':
        playNote(523.25, .25)
    if event.keysym == 'd':
        playNote(587.33, .25)
    if event.keysym == 'e':
        playNote(659.36, .25)

    #root.after(1, root.unbind, '<KeyPress>')
    #root.unbind('<KeyPress>')
    #root.bind('<KeyRelease>', keyReleaseFunc)
    #root.after(1, root.bind, '<KeyRelease>', keyReleaseFunc)


# def keyFunc(event): print 'Key', event.keysym
# text.bind('<Key>', keyFunc) # Same as KeyPress

#def keyReleaseFunc(event):
#    print 'in keyReleaseFunc'
    #global pressed
    #pressed = False
#    mySound.stop()
    #root.after(1, root.bind, '<KeyPress>', keyPressFunc)
    #root.after(1, root.unbind, '<KeyRelease>')
    #root.bind('<Key>', keyPressFunc)
    #time.sleep(1)

#root.bind('<KeyPress>', keyPressFunc)
#root.bind('<KeyRelease>', keyReleaseFunc)


def main():


    #button = Tkinter.Button(root, text='Play Tune', command=playTune2)

    #button.pack()


    #root.mainloop()



    #stdio.writeln('Playing')
    #playFile('woman.wav')

    stdio.writeln('Creating')
    sps = SAMPLE_RATE
    while not stdio.isEmpty():
        pitch = stdio.readInt()
        duration = stdio.readFloat()
        hz = 440 * math.pow(2, pitch / 12.0)
        N = int(sps * duration)
        notes = []
        for i in range(N+1):
            notes.append(math.sin(2*math.pi * i * hz / sps))
        stdio.writeln('Playing')
        playNotes(notes)

    root.mainloop()

    #stdio.writeln('Saving')
    #save('xxx.wav', notes)
    #stdio.writeln('Reading')
    #notes = read('xxx.wav')
    #stdio.writeln('Playing')
    #playNotes(notes)

if __name__ == '__main__':
    main()
