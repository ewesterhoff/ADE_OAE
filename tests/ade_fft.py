#!/usr/bin/env python

from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
import scipy.io.wavfile

m4a = AudioSegment.from_file('880.m4a')
m4a.export("880.wav", format="wav")

rate,audio = scipy.io.wavfile.read("880.wav")

fourier = fft.fft(audio)
fourier_abs = np.abs(fourier)
#fourier_abs = fourier

n = len(fourier_abs)
fourier_abs = fourier_abs[0:(n/2)]

fourier_abs = fourier_abs / float(n)

freqArray = np.arange(0, (n/2), 1.0) * (rate*1.0/n)

#plt.plot(fourier_abs, color='#ff7f00')
plt.plot(freqArray/1000, 10*np.log10(fourier_abs), color='#ff1f00', linewidth = 0.02)
plt.xlabel('Frequency (kHz)')
plt.xlim((0,8))
plt.ylabel('Power (dB)')
plt.show()
