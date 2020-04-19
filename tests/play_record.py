import pydub
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
import scipy.io.wavfile

import sounddevice as sd


#create soundfiles
#A4
m4_440 = AudioSegment.from_file('440_tone.mp4')
print(type(m4_440))
m4_440.export("440_tone.wav", format="wav")
rate, soundfile440 = scipy.io.wavfile.read("440_tone.wav")

#C5
#soundfile523 =

#A5
#soundfile880 =

errors = sd.CallbackFlags()
#sd.default.latency = ('hight', 'high')
fs = 44100
recording = sd.playrec(soundfile440, fs, channels=2)
print(errors)

channel1 = recording[:,0]

audio_segment = pydub.AudioSegment(
    channel1.tobytes(),
    frame_rate=fs,
    sample_width=channel1.dtype.itemsize,
    channels=1
)

audio_segment.export("soundfile440.wav", format = "wav")
#fourier = fft.fft(audio)
#fourier_abs = np.abs(fourier)
#fourier_abs = fourier

#n = len(fourier_abs)
#fourier_abs = fourier_abs[0:(n/2)]

#fourier_abs = fourier_abs / float(n)

#freqArray = np.arange(0, (n/2), 1.0) * (rate*1.0/n)

#plt.plot(fourier_abs, color='#ff7f00')
#plt.plot(freqArray/1000, 10*np.log10(fourier_abs), color='#ff1f00', linewidth = 0.02)
#plt.xlabel('Frequency (kHz)')
#plt.xlim((0,8))
#plt.ylabel('Power (dB)')
#plt.show()
