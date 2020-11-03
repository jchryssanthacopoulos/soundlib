# Record sound to numpy file
#
# Usage is: python record.py <filename> [<duration>]
#
# Default duration is 5 seconds
#
# Examples:
#   python.py record.py test.npy 5
#   python.py record.py test.npy
#

import sys

import numpy as np
import sounddevice as sd


SAMPLE_RATE = 44100
CHANNELS = 1 


def record(filename, duration): 
    my_recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS)
    sd.wait()
    np.save(filename, my_recording)


if __name__ == '__main__':
    filename = sys.argv[1]
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    record(filename, duration)
 
