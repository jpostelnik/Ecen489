import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.signal import welch

# Given parameters
Fs = 112e9  # Sampling frequency
M = 2**10   # FFT size
DF = 2497   # Decimation Factor
FsD = Fs / DF
c = 1e6  # Penalty constant (tunable)

# Function to solve for Fin
def func(Fin):
    R1 = np.round(Fin / Fs)
    R1D = np.round(Fin / FsD)
    Fa = abs(Fin - R1 * Fs)
    FaD = abs(Fin - R1D * FsD)
    kD = (FsD / 2 - FaD) * M / FsD
    kD_rounded = np.round(kD)
    FaD1 = FsD / 2 - kD_rounded * FsD / M
    return DF - (Fa / FaD) + c * (FaD1 - FaD)

# Initial guess for Fin
Fin_initial_guess = 22e9

# Solve for Fin
Fin_solution = fsolve(func, Fin_initial_guess)[0]

# Generate a signal for PSD plot
Fs_range = np.linspace(21e9, 23e9, 1000)
signal = np.sin(2 * np.pi * Fin_solution * np.arange(0, 1e-6, 1/Fs))

# Compute PSD using Welch's method
frequencies, psd = welch(signal, Fs, nperseg=256)

# Plot PSD
plt.figure(figsize=(10, 5))
plt.semilogy(frequencies, psd, label="Power Spectral Density")
plt.axvline(Fin_solution, color='red', linestyle='--', label=f"Solved Fin = {Fin_solution:.2e} Hz")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectral Density (dB/Hz)")
plt.title("PSD of Signal with Solved Fin")
plt.legend()
plt.grid()
plt.show()

print(f"Solved Fin: {Fin_solution:.2e} Hz")
