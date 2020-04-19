import numpy as np
import soundfile as sf
import sounddevice as sd
import pydub
from pydub import AudioSegment

weight = 1.4
length = 100000

a1 = AudioSegment.from_file('440.mp4')
a1.export("a_tone.wav", format="wav")

a2 = AudioSegment.from_file('c_drone.mp4')
a2.export("c_tone.wav", format="wav")

data_left, fs_left = sf.read('a_tone.wav')
data_right, fs_right = sf.read('c_tone.wav', frames=len(data_left), fill_value=0)

data_left_mono = data_left[:,0]
data_right_mono = data_right[:,0]

assert fs_left == fs_right
assert data_left_mono.ndim == data_right_mono.ndim == 1

data_stereo = np.column_stack([data_left_mono, weight*data_right_mono])
print(data_stereo)
#sd.play(data_stereo, fs_left)
#sd.wait()

recording = sd.playrec(data_stereo, fs_left, channels=3)
sd.wait()
#print(errors)

data_r = recording[:,0]

shifted = data_r * (2 ** 31 - 1)   # Data ranges from -1.0 to 1.0
data_ints = shifted.astype(np.int32)

audio_segment = pydub.AudioSegment(
    data_ints.tobytes(),
    frame_rate=fs_left,
    #sample_width=channel1.dtype.itemsize,
    sample_width = 4,
    channels=1
)

audio_segment.export("test2.wav", format = "wav")
