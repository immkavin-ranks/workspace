import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
A = 1.0    # Amplitude for f1
w = 2.0    # Angular frequency for f1
tau = 1.0  # Decay time constant for f1

B = 0.5    # Amplitude for f2
w2 = 1.5   # Angular frequency for f2

# Define the time values
t = np.linspace(0, 10, 1000)  # Time values from 0 to 10, 1000 points

# Define the functions f1(t, w, tau, A) and f2(t, w, w2, B)
f1 = A * np.cos(w * t) * np.exp(-t / tau)
f2 = B * np.sin(w2) * np.sin(w * t)

# Create two subplots for f1 and f2
plt.figure(figsize=(12, 6))

# Plot f1
plt.subplot(2, 1, 1)
plt.plot(t, f1, label='$A\cos(wt)e^{-t/\\tau}$', color='blue')
plt.xlabel('Time (t)')
plt.ylabel('$f_1(t, w, \\tau, A)$')
plt.title('Plot of $f_1(t, w, \\tau, A)$')
plt.legend()

# Plot f2
plt.subplot(2, 1, 2)
plt.plot(t, f2, label='$B\sin(w_2)\sin(wt)$', color='red')
plt.xlabel('Time (t)')
plt.ylabel('$f_2(t, w, w_2, B)$')
plt.title('Plot of $f_2(t, w, w_2, B)$')
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
