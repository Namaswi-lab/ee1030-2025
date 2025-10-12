import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define ranges for x and y
x = np.linspace(-2, 6, 30)
y = np.linspace(-2, 6, 30)
X, Y = np.meshgrid(x, y)

# Define the three planes:  Ax + By + Cz = D
Z1 = (4 - 2*X - 0*Y) / 2           # 2x + 0y + 2z = 4
Z2 = (4 - 3*X - 7*Y) / 2           # 3x + 7y + 2z = 4
Z3 = (5 - 5*X - 1*Y) / 7           # 5x + y + 7z = 5

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color='r')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='g')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='b')

# Intersection point (unique solution)
x_sol, y_sol, z_sol = 21/5, -3/5, -11/5
ax.scatter(x_sol, y_sol, z_sol, color='k', s=80)

# Axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Three Planes: Unique Solution')

# Add clear labels in different areas of the plot
ax.text(-1.5, -1.5, 4, 'Plane 1:\n$2x + 2z = 4$', color='r', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='r', alpha=0.7))

ax.text(5, 5, 3, 'Plane 2:\n$3x + 7y + 2z = 4$', color='g', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='g', alpha=0.7))

ax.text(1, 5, -3, 'Plane 3:\n$5x + y + 7z = 5$', color='b', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='b', alpha=0.7))

# Label the intersection point
ax.text(x_sol + 0.5, y_sol, z_sol + 0.5,
        'Unique Solution\n({:.2f}, {:.2f}, {:.2f})'.format(x_sol, y_sol, z_sol),
        color='k', fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='k', alpha=0.7))

plt.show()
