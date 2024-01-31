import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Simulation parameters
room_width = 10   # Width of the room (in grid cells)
room_height = 10  # Height of the room (in grid cells)
room_depth = 10   # Depth of the room (in grid cells)
c = 343           # Speed of sound in air (m/s)
dx = 1            # Spatial step size (meters)
dt = 0.001        # Time step size (seconds)
duration = 1.0    # Duration of simulation (seconds)

# Initialize arrays
num_steps = int(duration / dt)
num_x_cells = int(room_width / dx)
num_y_cells = int(room_height / dx)
num_z_cells = int(room_depth / dx)
u = np.zeros((num_x_cells, num_y_cells, num_z_cells, num_steps+1))

# Initial condition: Gaussian pulse as sound source
source_x = num_x_cells // 2
source_y = num_y_cells // 2
source_z = num_z_cells // 2
u[source_x, source_y, source_z, 0] = 2

# Finite difference loop for time integration
for n in range(1, num_steps):
    for i in range(1, num_x_cells - 1):
        for j in range(1, num_y_cells - 1):
            for k in range(1, num_z_cells - 1):
                laplacian = (
                    u[i+1, j, k, n-1] + u[i-1, j, k, n-1] +
                    u[i, j+1, k, n-1] + u[i, j-1, k, n-1] +
                    u[i, j, k+1, n-1] + u[i, j, k-1, n-1] - 6 * u[i, j, k, n-1]
                )
                u[i, j, k, n] = 2 * u[i, j, k, n-1] - u[i, j, k, n-2] + (c * dt / dx)**2 * laplacian

# Visualization using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = np.meshgrid(np.arange(num_x_cells), np.arange(num_y_cells), np.arange(num_z_cells))
ax.voxels(u[:, :, :, 0], facecolors='blue', edgecolor='k', alpha=0.5)

def animate(n):
    ax.clear()
    ax.voxels(u[:, :, :, n], facecolors='blue', edgecolor='k', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Acoustic Wave Propagation in a 3D Room')

anim = FuncAnimation(fig, animate, frames=num_steps, interval=50, blit=False)

plt.show()
