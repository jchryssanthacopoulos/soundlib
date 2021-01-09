# Record sound to file."""

import argparse
import os
import time

import numpy as np
from scipy.io import wavfile
import sounddevice as sd


CHANNELS = 1


def record(filename, duration, sample_rate, fmt): 
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
    parser.add_argument('-o', '--output', type=str, required=True, help='Name of output file')
    parser.add_argument('-d', '--duration', type=int, required=True, help='Duration in seconds')
    parser.add_argument('-s', '--sample-rate', type=int, required=True, help='Sample rate in samples per second')
    parser.add_argument('-n', '--num-recordings', type=int, default=1, help='Number of recordings to make')
    parser.add_argument('--format', choices=['npy', 'wav'], default='npy', help='Format to save recording in')
    arguments = parser.parse_args()

    if arguments.num_recordings == 1:
        print("Recording...")
        record(arguments.output, arguments.duration, arguments.sample_rate, arguments.format)
    else:
        filename_no_ext, filename_ext = os.path.splitext(arguments.output)
        for i in range(arguments.num_recordings):
            recording_filename = f"{filename_no_ext}.{i + 1}{filename_ext}"
            print(f"Recording {i + 1}")
            record(recording_filename, arguments.duration, arguments.sample_rate, arguments.format)
            print(f"End {i + 1}\n")
            time.sleep(0.5)
