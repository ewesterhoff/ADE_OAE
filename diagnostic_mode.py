import numpy as np
import soundfile as sf
import sounddevice as sd
import pydub
from pydub import AudioSegment

#balances for natural variation in volumne
weight = 1.4

#can be used to limit the length of the sound file
#TO DO: implement
length = 100000

#convert to usable file format
#shouldn't be needed in final
#TO DO: Create seperate script for this conversion
a1 = AudioSegment.from_file('440.mp4')
a1.export("a_tone.wav", format="wav")

a2 = AudioSegment.from_file('c_drone.mp4')
a2.export("c_tone.wav", format="wav")

#Import sound files as data
#TO DO: Index into folder with all files
data_left, fs_left = sf.read('a_tone.wav')
data_right, fs_right = sf.read('c_tone.wav', frames=len(data_left), fill_value=0)

#Convert sound files to mono files (left, right)
data_left_mono = data_left[:,0]
data_right_mono = data_right[:,0]

#Assert identical sampling frequencies
assert fs_left == fs_right
#Assert mono files
assert data_left_mono.ndim == data_right_mono.ndim == 1

#Combine mono files into stero file
data_stereo = np.column_stack([data_left_mono, weight*data_right_mono])

#Play stereo file
#sd.play(data_stereo, fs_left)
#sd.wait()

#Play stero file, and record from the third channel
recording = sd.playrec(data_stereo, fs_left, channels=3)
sd.wait()

#Get recording data
data_r = recording[:,0]

#Map data to integer representation
#See: https://github.com/jiaaro/pydub/issues/293

shifted = data_r * (2 ** 31 - 1)   # Data ranges from -1.0 to 1.0
data_ints = shifted.astype(np.int32)

#ave data to audio file
audio_segment = pydub.AudioSegment(
    data_ints.tobytes(),
    frame_rate=fs_left,
    #sample_width=channel1.dtype.itemsize,
    sample_width = 4,
    channels=1
)
audio_segment.export("test2.wav", format = "wav")
