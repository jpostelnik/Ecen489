import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Given parameters
F1 = 200e6  # Frequency of first cosine wave (Hz)
Fs_values = [500e6, 800e6, 1000e6]  # Sampling frequencies
T = 10 / F1  # Duration (10 cycles of cosine wave)

# Time vector for continuous signal
continuous_time = np.linspace(0, T, 1000)
x1 = np.cos(2 * np.pi * F1 * continuous_time)

# Reconstruction using sinc interpolation
def sinc_interp(x_samples, t_samples, t, Ts):
    return np.sum(x_samples[:, None] * np.sinc((t - t_samples[:, None]) / Ts), axis=0)

for Fs in Fs_values:
    Ts = 1 / Fs  # Sampling interval
    
    # Time vectors
    n_samples = np.arange(0, T, Ts)
    shifted_samples = np.arange(Ts/2, T - Ts/2, Ts)
    
    # Sample the signal
    x1_samples = np.cos(2 * np.pi * F1 * n_samples)
    x1_shifted_samples = np.cos(2 * np.pi * F1 * shifted_samples)
    
    # Reconstruct signal
    x1_reconstructed = sinc_interp(x1_samples, n_samples, continuous_time, Ts)
    x1_shifted_reconstructed = sinc_interp(x1_shifted_samples, shifted_samples, continuous_time, Ts)
    
    # Compute Mean Squared Error (MSE)
    MSE1 = np.mean((x1_reconstructed - x1) ** 2)
    MSE2 = np.mean((x1_shifted_reconstructed - x1) ** 2)
    
    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(continuous_time, x1, label="Original Signal", linestyle='dashed')
    plt.plot(continuous_time, x1_reconstructed, label=f"Reconstructed (0:Ts:T-Ts), Fs={Fs/1e6} MHz")
    plt.plot(continuous_time, x1_shifted_reconstructed, label=f"Reconstructed (Ts/2:Ts:T-Ts/2), Fs={Fs/1e6} MHz")
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"Signal Reconstruction Using Sinc Interpolation (Fs={Fs/1e6} MHz)")
    plt.grid()
    plt.show()
    
    # Print MSE values
    print(f"Fs = {Fs/1e6} MHz")
    print(f"MSE (0:Ts:T-Ts) = {MSE1}")
    print(f"MSE (Ts/2:Ts:T-Ts/2) = {MSE2}\n")
