import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk

# FIR Filter Coefficients (H_FIR(z) = 1 + 0.5z^-1 + 0.25z^-2)
b_fir = [1, 1, 1, 1,1]  # Numerator
a_fir = [1]             # Denominator (FIR has no feedback)

# Compute Frequency Response
w_fir, h_fir = freqz(b_fir, a_fir, worN=1024)

# Compute Poles and Zeros
zeros_fir, poles_fir, _ = tf2zpk(b_fir, a_fir)

# Plot Frequency Response
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# FIR Filter - Magnitude Response
ax[0].plot(w_fir / np.pi,20*np.log10( abs(h_fir)), 'b')
ax[0].set_title('Magnitude Response')
ax[0].grid()

# Plot Pole-Zero Diagram
ax[1].scatter(np.real(zeros_fir), np.imag(zeros_fir), color='b', marker='o', label='FIR Zeros')
ax[1].scatter(np.real(poles_fir), np.imag(poles_fir), color='b', marker='x', label='FIR Poles')
ax[1].axhline(0, color='black', linewidth=0.5)
ax[1].axvline(0, color='black', linewidth=0.5)
ax[1].grid()
ax[1].legend()
ax[1].set_title("Pole-Zero Diagram")
plt.tight_layout()
plt.show()
