# Play sound from numpy file
#
# Usage is: python play.py <filename>
#
# Examples:
#   python.py play.py test.npy
#

import sys

import numpy as np
import sounddevice as sd


SAMPLE_RATE = 44100


def play(filename):
    recording = np.load(filename)
    sd.play(recording, SAMPLE_RATE)
    sd.wait()


if __name__ == '__main__':
    filename = sys.argv[1]
    play(filename)
 
