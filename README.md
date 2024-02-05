# soundlib
Record and play audio files with Python.

## Install

This software has been tested in Python 3.7.9. If you use pyenv, the right version will be set automatically from `.python-version`. 

In a virtual environment, run

```
pip install -r requirements.txt
```

## Record Sound

To record sound, run

```
python record.py -o OUTPUT -d DURATION -s SAMPLE_RATE [--format {npy,wav}]
```

This saves either a numpy or wav file, depending on the format chosen. The default is npy.

## Play Sound

To play the sound file, run

```
python play.py -i INPUT -s SAMPLE_RATE [--format {npy,wav}]
```

The input can be either a single file or a directory containing several files. If a directory, the files are played sequentially.

## Examples

```
# record a numpy file for 3 seconds at 44100 Hz and play it back
python record.py -o test.npy -d 3 -s 44100
python play.py -i test.npy -s 44100

# record a wav file for 4 seconds at 8000 Hz and play it back
python record.py -o test.wav -d 4 -s 8000 --format wav
python play.py -i test.wav -s 8000 --format wav
```
