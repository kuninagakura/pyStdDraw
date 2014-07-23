#-----------------------------------------------------------------------
# guitarhero.py
#-----------------------------------------------------------------------

import stdaudio
import stddrawtkinter as stddraw
import guitarstring

#-----------------------------------------------------------------------

_CONCERT_A = 440.0
_KEYBOARD = 'q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/\' '

#-----------------------------------------------------------------------

def main():

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

    # loopCount is used to control the frequency of calls of
    # stddraw.show().
    loopCount = 1023

    # The main input loop.
    while True:

        # Call stddraw.show() occasionally to capture keyboard events.
        if loopCount == 1023:
            stddraw.show()
            loopCount = 0
        loopCount += 1

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
        for guitarString in pluckedGuitarStrings:
            sample += guitarString.sample()
            guitarString.tic()

        # Play the total.
        stdaudio.playSample(sample)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
