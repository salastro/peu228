import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
I_0 = 1.0  # Current (A)
epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
omega = 1e3  # Angular frequency (rad/s)

# Figure setup
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Plot 1: B = (mu_0 * I * np.log(r))/(np.pi * r)
r1 = np.linspace(0, 10, 400)
B1 = (mu_0 * I_0 * np.log(r1+1))/(np.pi * r1)
axs[0].plot(r1, B1, label=r'$\mathbf{B} = \frac{\mu_{0}I}{\pi r} \ln(r) \hat{z}$', color='g')
axs[0].set_xlabel(r'Distance $r$ (m)')
axs[0].set_ylabel(r'Magnetic Field $B$ (T)')
axs[0].set_title(r'Plot of $\mathbf{B} = \frac{\mu_{0}I}{\pi r} \ln(r) \hat{z}$')
axs[0].legend()
axs[0].grid(True)

# Plot 2: B(r, t) as a function of distance r
r2 = np.linspace(0.1, 10, 400)
B2 = (mu_0 * I_0 / (2 * np.pi * r2)) * np.cos(omega * 0) * (1 + 1 / (2 * epsilon_0 * omega**2 * r2**2))
axs[1].plot(r2, B2, label=r'$B(r, t) = \frac{\mu_0 I_0}{2 \pi r} \cos(\omega t) \left(1 + \frac{1}{2 \epsilon_0 \omega^2 r^2}\right)$', color='b')
axs[1].set_xlabel(r'Distance $r$ (m)')
axs[1].set_ylabel(r'Magnetic Field $B$ (T)')
axs[1].set_title(r'Plot of $B(r, t)$ as a function of distance $r$')
axs[1].legend()
axs[1].grid(True)

# Plot 3: B(r, t) as a function of time t
r3 = 1.0  # Fixed distance (m)
t3 = np.linspace(0, 0.01, 400)
B3 = (mu_0 * I_0 / (2 * np.pi * r3)) * np.cos(omega * t3) * (1 + 1 / (2 * epsilon_0 * omega**2 * r3**2))
axs[2].plot(t3, B3, label=r'$B(r, t) = \frac{\mu_0 I_0}{2 \pi r} \cos(\omega t) \left(1 + \frac{1}{2 \epsilon_0 \omega^2 r^2}\right)$', color='r')
axs[2].set_xlabel(r'Time $t$ (s)')
axs[2].set_ylabel(r'Magnetic Field $B$ (T)')
axs[2].set_title(r'Plot of $B(r, t)$ as a function of time $t$ for fixed $r$')
axs[2].legend()
axs[2].grid(True)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the combined plot
plt.show()

