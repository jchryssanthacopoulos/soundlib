# soundlib
Record and play audio files with Python.

## Install

This software has been tested in Python 3.6.12. If you use pyenv, the right version will be set automatically from `.python-version`. 

In a virtual environment, run

```
pip install -r requirements.txt
```

## Record Sound

To record sound, run

```
python record.py <filename> [<duration_in_seconds>]
```

This saves a numpy file with the sound array data.

## Play Sound

To play sound from a numpy file, run

```
python play.py <filename>
```

## Example

```
# record for 10 seconds and play it back
python record.py test.npy 10
python play.py test.npy
```
