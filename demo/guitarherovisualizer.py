#-----------------------------------------------------------------------
# guitarherovisualizer.py
#-----------------------------------------------------------------------

import stdaudio
import stddrawDialogProcesses as stddraw
import guitarstring

#-----------------------------------------------------------------------

_CONCERT_A = 440.0
_KEYBOARD = 'q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/\' '
_SAMPLES_PER_REDRAW = 4410

#-----------------------------------------------------------------------

def main():

    stddraw.createWindow(1024, 256)
    stddraw.setPenRadius(0)
    stddraw.setXscale(0, _SAMPLES_PER_REDRAW)
    stddraw.setYscale(-.75, +.75)
    stddraw.show()

    # Create keyboardDict, a dictionary relating each keyboard key
    # to a guitar string.
    keyboardDict = {}
    i = 0
    for key in _KEYBOARD:
        factor = 2 ** ((i-24) / 12.0)
        guitarString = guitarstring.GuitarString(_CONCERT_A * factor)
        keyboardDict[key] = guitarString
        i += 1

    # pluckedGuitarStrings is the set of all guitar strings that have
    # been plucked.
    pluckedGuitarStrings = set()

    t = 0

    # The main input loop.
    while True:

        if stddraw.hasNextKeyTyped():

            # Fetch the key that the user just typed.
            key = stddraw.nextKeyTyped()

            # Figure out which guitar string to pluck, and pluck it.
            try:
                guitarString = keyboardDict[key]
                guitarString.pluck()
                pluckedGuitarStrings.add(guitarString)
            except KeyError:
                pass

        # Add up the samples from each plucked guitar string. Also
        # advance the simulation of each plucked guitar string by
        # one step.
        sample = 0.0
        faintGuitarStrings = set()
        for guitarString in pluckedGuitarStrings:
            sample += guitarString.sample()
            guitarString.tic()
            if guitarString.isFaint():
                faintGuitarStrings.add(guitarString)

        # Remove faint guitar strings from the set of plucked guitar
        # strings.
        for guitarString in faintGuitarStrings:
            pluckedGuitarStrings.remove(guitarString)

        # Play the total.
        stdaudio.playSample(sample)

        # Plot
        stddraw.point(t % _SAMPLES_PER_REDRAW, sample);

        if t == (_SAMPLES_PER_REDRAW - 1):
            stddraw.show()
            stddraw.clear()
            t = 0

        t += 1

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
