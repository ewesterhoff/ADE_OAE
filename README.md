# ADE_OAE

## Purpose of Project
will go here

## Tests
contains outdated tests that are of no use to this project

## Tones
contains a script "generate_tones.py" to generate 3 second long .wav files consisting of pure generate_tones
tones will be named with the convention "440.00_hz.wav" for a tone at 440.00 hz


## diagnostic_mode.py
currently consists of a basic play-record test. will work with the rest of the team to determine functionality of this mode.

## test_mode.py
currently consists of a basic play-record test. features to be added:
automatic amplitude detection of DP (fft math is done, just need to make automatic with filenames and integrate into this code)
automatic sweep through of all required frequencies for screening (will compile a list compliant with IEC standard)
