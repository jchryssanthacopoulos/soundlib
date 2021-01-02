# Record sound to file."""

import argparse

import numpy as np
from scipy.io import wavfile
import sounddevice as sd


CHANNELS = 1


def record(filename, duration, sample_rate, fmt): 
    print("Recording...")
    my_recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=CHANNELS)
    sd.wait()
    if fmt == 'wav':
        # save as wav file
        wavfile.write(filename, sample_rate, my_recording)
    else:
        # save as npy file
        np.save(filename, my_recording)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Record sound')
    parser.add_argument('-o', '--output', type=str, required=True,
        help='Name of output file')
    parser.add_argument('-d', '--duration', type=int, required=True,
        help='Duration in seconds')
    parser.add_argument('-s', '--sample-rate', type=int, required=True,
        help='Sample rate in samples per second')
    parser.add_argument('--format', choices=['npy', 'wav'], default='npy',
        help='Format to save recording in')
    arguments = parser.parse_args()

    record(arguments.output, arguments.duration, arguments.sample_rate, arguments.format)
