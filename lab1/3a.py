import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Given parameters
F = 2e6  # Frequency of the signal (Hz)
Fs = 5e6  # Sampling frequency (Hz)
N = 50    # Number of points for DFT

# Time vector
T = 1 / Fs
n = np.arange(N)
x = np.cos(2 * np.pi * F * n * T)  # Sampled signal

# Compute the DFT using FFT
X = fft(x, N)
frequencies = fftfreq(N, T)  # Frequency axis

# Plot magnitude spectrum
plt.figure(figsize=(8, 4))
plt.stem(frequencies[:N//2], np.abs(X[:N//2]), use_line_collection=True)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Magnitude Spectrum of the Sampled Signal")
plt.grid()
plt.show()
