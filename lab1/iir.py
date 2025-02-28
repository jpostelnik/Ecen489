import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk

# iir Filter Coefficients (H_iir(z) = 1 + 0.5z^-1 + 0.25z^-2)
b_iir = [1,1]  # Numerator
a_iir = [1,-1]             # Denominator (iir has no feedback)

# Compute Frequency Response
w_iir, h_iir = freqz(b_iir, a_iir, worN=1024)

# Compute Poles and Zeros
zeros_iir, poles_iir, _ = tf2zpk(b_iir, a_iir)

# Plot Frequency Response
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# iir Filter - Magnitude Response
ax[0].plot(w_iir / np.pi,20*np.log10( abs(h_iir)), 'b')
ax[0].set_title('Magnitude Response')
ax[0].grid()

# Plot Pole-Zero Diagram
ax[1].scatter(np.real(zeros_iir), np.imag(zeros_iir), color='b', marker='o', label='iir Zeros')
ax[1].scatter(np.real(poles_iir), np.imag(poles_iir), color='b', marker='x', label='iir Poles')
ax[1].axhline(0, color='black', linewidth=0.5)
ax[1].axvline(0, color='black', linewidth=0.5)
ax[1].grid()
ax[1].legend()
ax[1].set_title("Pole-Zero Diagram")
plt.tight_layout()
plt.show()
