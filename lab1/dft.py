import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Given parameters
F = 2e6  # Frequency of the cosine wave (Hz)
Fs = 5e6  # Sampling frequency (Hz)
N = 50    # Number of DFT points

# Time vector (sampled at Fs)
t = np.arange(N) / Fs

# Generate the sampled cosine wave
x = np.cos(2 * np.pi * F * t)

# Compute the DFT using FFT
X = fft(x, N)
frequencies = fftfreq(N, d=1/Fs)  # Frequency axis

# Plot the magnitude spectrum
plt.figure(figsize=(8, 4))
plt.stem(frequencies[:N//2], np.abs(X[:N//2]))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("50-Point DFT of x(t) = cos(2πFt) with Fs = 5 MHz")
plt.grid()
plt.show()
