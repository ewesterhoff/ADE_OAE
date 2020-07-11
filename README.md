# ADE_OAE

## Purpose of Project
Develop suite of software to prototype, test, and eventually deploy a low-cost OAE screening device.

## Status of Project
The project is currently at a proof-of-concept stage. Software development is being done in python for several reasons: it is accessible to most students at Olin, and at the time of writing there is no need for a more robust language. The team has not currently determined if this technology will be a standalone device, a smartphone application, or something to run alongside a full computer. Future work on this portion of the project should align with the progress of the team in this way, and should not push the team into taking one technical direction over the other. See the 2020 spring readme for more information.

See 2020 Spring Readme in the Google Drive folder for a more robust status report.

## Tests
Contains outdated tests that are of no use to this project. Future files moved to this folder should be well documented to allow future teams to reuse the code if it becomes useful again.

## Tones
Contains a script "generate_tones.py" to generate 3 second long .wav files consisting of pure tones at a single frequency
Tones should be named with the convention "440.00_hz.wav" for a tone at 440.00 hz for ease of sweeping through multiple tones in a test
These tones are accessed and played by other files in the directory

## diagnostic_mode.py
Currently consists of a basic play-record test. This mode was created to be run to meet the IEC requirements for volume, noise reduction, power draw, etc. This mode is not done, but rather creates a seperate framework for testing the properties of the device.

## test_mode.py
This program contains code to "do the job" of the device, and currently consists of a basic play-record test. 
Features to be added:
-Automatic amplitude detection of DP. Some information can be gleaned through raw amplitudes rather than just comparisons with the standard (see 2020 spring readme for more information)
-Automatic sweep through of all required frequencies for screening. These frequencies must be consistent and compliant with IEC standard.

## Contact
Emma Westerhoff (etwesterhoff@gmail.com) was a developer on this project who is happy to answer questions about technical content or project decisions made in the codebase dated at or before July 2020. 


