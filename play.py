# Play sound from numpy file
#
# Usage is: python play.py <filename> <sample_rate>
#
# Examples:
#   python.py play.py test.npy 8000
#

import argparse

import numpy as np
from scipy.io import wavfile
import sounddevice as sd


def play(filename, sample_rate, fmt):
    if fmt == 'wav':
        sample_rate, recording = wavfile.read(filename)
    else:
        recording = np.load(filename)
    sd.play(recording, sample_rate)
    sd.wait()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play sound')
    parser.add_argument('-i', '--input', type=str, required=True,
        help='Name of input file')
    parser.add_argument('-s', '--sample-rate', type=int, required=True,
        help='Sample rate in samples per second')
    parser.add_argument('--format', choices=['npy', 'wav'], default='npy',
        help='Format of input file')
    arguments = parser.parse_args()

    play(arguments.input, arguments.sample_rate, arguments.format)
 