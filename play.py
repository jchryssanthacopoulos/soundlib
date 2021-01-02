# Play sound from file or directory."""

import argparse
import glob
import os
import sys
import time

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
        help='Name of input file or directory')
    parser.add_argument('-s', '--sample-rate', type=int, required=True,
        help='Sample rate in samples per second')
    parser.add_argument('--format', choices=['npy', 'wav'], default='npy',
        help='Format of input file')
    arguments = parser.parse_args()

    if os.path.isdir(arguments.input):
        # loop through files
        for sound_file in sorted(glob.glob(f"{arguments.input}/*.{arguments.format}")):
            print(f"Playing {sound_file}...")
            play(sound_file, arguments.sample_rate, arguments.format)
            time.sleep(0.5)
        sys.exit()

    # play single file
    play(arguments.input, arguments.sample_rate, arguments.format)
 