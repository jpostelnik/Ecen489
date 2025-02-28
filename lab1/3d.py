import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import blackman

# Given parameters
F1 = 200e6  # Frequency of first component (Hz)
F2 = 500e6  # Frequency of second component (Hz)
Fs = 1e9    # Sampling frequency (Hz)
N = 50      # Number of points for DFT

# Time vector
T = 1 / Fs
n = np.arange(N)
y = np.cos(2 * np.pi * F1 * n * T) + np.cos(2 * np.pi * F2 * n * T)  # Sampled signal

# Apply Blackman window
window = blackman(N)
y_windowed = y * window

# Compute the DFT using FFT
Y = fft(y_windowed, N)
frequencies = fftfreq(N, T)  # Frequency axis

# Plot magnitude spectrum
plt.figure(figsize=(8, 4))
plt.stem(frequencies[:N//2], np.abs(Y[:N//2]), use_line_collection=True)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Magnitude Spectrum with Blackman Window")
plt.grid()
plt.show()
