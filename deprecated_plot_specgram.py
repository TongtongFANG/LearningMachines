import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import sys

X, sample_rate = librosa.load(sys.argv[1], sr=None)

spectrum,freqs,t,_ = specgram(X, Fs=sample_rate)

print(spectrum.shape)
print(freqs.shape)
print(t.shape)

plt.show()