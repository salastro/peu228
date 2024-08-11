import numpy as np
import matplotlib.pyplot as plt

# Constants
mu0 = 4 * np.pi * 1e-7  # Permeability of free space
I0 = 1  # Amplitude of current
omega = 2 * np.pi * 60  # Angular frequency (assuming 60 Hz)
epsilon0 = 8.854e-12  # Permittivity of free space

# Create a grid
x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
X, Y = np.meshgrid(x, y)

# Calculate polar coordinates
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Function for alternating current case
def B_alternating(R, Theta, t):
    B_magnitude = (mu0 * I0 / (2 * np.pi * R)) * np.cos(omega * t) * (1 + 0.5 * epsilon0 * omega**2 * R**2)
    Bx = -B_magnitude * np.sin(Theta)
    By = B_magnitude * np.cos(Theta)
    return Bx, By, B_magnitude

# Function for steady current case with logarithmic dependence
def B_steady(R, Theta):
    B_magnitude = (mu0 * I0 * np.log(R+1))/(np.pi * R)
    Bx = -B_magnitude * np.sin(Theta)
    By = B_magnitude * np.cos(Theta)
    return Bx, By, B_magnitude

# Normalize vectors
def normalize_vectors(Bx, By):
    B_total = np.sqrt(Bx**2 + By**2)
    return Bx/B_total, By/B_total

# Create figures
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot alternating current case (at t=0)
Bx1, By1, B_mag1 = B_alternating(R, Theta, 0)
Bx1_norm, By1_norm = normalize_vectors(Bx1, By1)
quiver1 = ax1.quiver(X, Y, Bx1_norm, By1_norm, B_mag1, cmap='viridis', scale=25, width=0.002)
ax1.set_title('Magnetic Field - Alternating Current (t=0)')
ax1.add_artist(plt.Circle((0, 0), 0.05, color='r'))  # Represent the wire
fig.colorbar(quiver1, ax=ax1, label='Field Strength')

# Plot steady current case
Bx2, By2, B_mag2 = B_steady(R, Theta)
Bx2_norm, By2_norm = normalize_vectors(Bx2, By2)
quiver2 = ax2.quiver(X, Y, Bx2_norm, By2_norm, B_mag2, cmap='viridis', scale=25, width=0.002)
ax2.set_title('Magnetic Field - Steady Current (Logarithmic)')
ax2.add_artist(plt.Circle((0, 0), 0.05, color='r'))  # Represent the wire
fig.colorbar(quiver2, ax=ax2, label='Field Strength')

# Set labels and limits
for ax in [ax1, ax2]:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')

plt.tight_layout()
plt.show()
