import numpy as np
import matplotlib.pyplot as plt

# Given frequencies
F1 = 300e6  # 300 MHz
F2 = 800e6  # 800 MHz
Fs = 500e6  # 500 MHz (sampling frequency)
Ts = 1 / Fs # Sampling period

# Time axis for continuous signals
t = np.linspace(0, 10e-9, 1000)  # 10 ns duration

# Continuous signals
x1_t = np.cos(2 * np.pi * F1 * t)
x2_t = np.cos(2 * np.pi * F2 * t)

# Sampled signals (discrete time)
n = np.arange(0, 20)  # 20 samples
x1_n = np.cos(2 * np.pi * (F1 / Fs) * n)  # Discrete-time representation
x2_n = np.cos(2 * np.pi * (F2 / Fs) * n)  # Discrete-time representation

# Create a 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(12, 6))

# Plot x1(t) (Continuous)
axes[0, 0].plot(t * 1e9, x1_t, label="x1(t) = cos(2π * 300MHz * t)", linestyle='dashed')
axes[0, 0].set_xlabel("Time (ns)")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].set_title("Continuous x1(t)")
axes[0, 0].grid()
axes[0, 0].legend()

# Plot x2(t) (Continuous)
axes[0, 1].plot(t * 1e9, x2_t, label="x2(t) = cos(2π * 800MHz * t)", linestyle='dashed', color='r')
axes[0, 1].set_xlabel("Time (ns)")
axes[0, 1].set_ylabel("Amplitude")
axes[0, 1].set_title("Continuous x2(t)")
axes[0, 1].grid()
axes[0, 1].legend()

# Plot x1(n) (Sampled)
axes[1, 0].stem(n, x1_n, linefmt='b-', markerfmt='bo', basefmt=" ", label="Sampled x1(n)")
axes[1, 0].set_xlabel("Sample index (n)")
axes[1, 0].set_ylabel("Amplitude")
axes[1, 0].set_title("Sampled x1(n)")
axes[1, 0].grid()
axes[1, 0].legend()

# Plot x2(n) (Sampled)
markerline, stemline, baseline = axes[1, 1].stem(n, x2_n, linefmt='r-', markerfmt='ro', basefmt=" ", label="Sampled x2(n)")
plt.setp(markerline, alpha=0.6)  # Set transparency
plt.setp(stemline, alpha=0.6)  # Set transparency
axes[1, 1].set_xlabel("Sample index (n)")
axes[1, 1].set_ylabel("Amplitude")
axes[1, 1].set_title("Sampled x2(n)")
axes[1, 1].grid()
axes[1, 1].legend()

# Adjust layout
plt.tight_layout()
plt.show()
