import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared object
solver = ctypes.CDLL('./solver.so')

# Define argument and return types
solver.solve3x3.argtypes = [
    (ctypes.c_float * 3) * 3,  # 3x3 matrix
    ctypes.c_float * 3,        # b vector
    ctypes.c_float * 3         # x output vector
]

# Define matrices
A = np.array([[2, 0, 2],
              [3, 7, 2],
              [5, 1, 7]], dtype=np.float32)
b = np.array([4, 4, 5], dtype=np.float32)

# Prepare ctypes arrays
A_ctypes = ((ctypes.c_float * 3) * 3)(*map(lambda r: (ctypes.c_float * 3)(*r), A))
b_ctypes = (ctypes.c_float * 3)(*b)
x_ctypes = (ctypes.c_float * 3)()

# Call C function
solver.solve3x3(A_ctypes, b_ctypes, x_ctypes)

# Convert result back to numpy
x = np.array(list(x_ctypes))
print("Solution from C function:", x)

# === Plot the planes ===
xv = np.linspace(-2, 6, 30)
yv = np.linspace(-2, 6, 30)
X, Y = np.meshgrid(xv, yv)
Z1 = (4 - 2*X - 0*Y) / 2
Z2 = (4 - 3*X - 7*Y) / 2
Z3 = (5 - 5*X - 1*Y) / 7

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, alpha=0.5, color='r')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='g')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='b')

# Plot intersection from C
ax.scatter(x[0], x[1], x[2], color='k', s=50, label='C Solver Intersection')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Planes (Solution from C Shared Library)')
ax.legend()

plt.show()
