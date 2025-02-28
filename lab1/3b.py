import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Given parameters
F1 = 200e6  # Frequency of first component (Hz)
F2 = 400e6  # Frequency of second component (Hz)
Fs = 1e9    # Sampling frequency (Hz)
N = 50      # Number of points for DFT

# Time vector
T = 1 / Fs
n = np.arange(N)
y = np.cos(2 * np.pi * F1 * n * T) + np.cos(2 * np.pi * F2 * n * T)  # Sampled signal

# Compute the DFT using FFT
Y = fft(y, N)
frequencies = fftfreq(N, T)  # Frequency axis

# Plot magnitude spectrum
plt.figure(figsize=(8, 4))
plt.stem(frequencies[:N//2], np.abs(Y[:N//2]), use_line_collection=True)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Magnitude Spectrum of the Sampled Signal")
plt.grid()
plt.show()
