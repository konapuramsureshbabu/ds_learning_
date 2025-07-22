import numpy as np 

# Set seed for reproducibility
np.random.seed(100)

# Create a 3D random matrix of shape (2, 3, 3)
matrix_3d = np.random.randint(1, 10, size=(2, 3, 3))

print("Original 3D Matrix:\n", matrix_3d)

# Sum along axis=0 (sum over depth -> keeps 3x3 shape)
print("\nSum over axis=0 (depth-wise sum):\n", np.sum(matrix_3d, axis=0))

# Sum along axis=1 (sum over rows in each matrix)
print("\nSum over axis=1 (row-wise within each matrix):\n", np.sum(matrix_3d, axis=1))

# Sum along axis=2 (sum over columns in each matrix)
print("\nSum over axis=2 (column-wise within each matrix):\n", np.sum(matrix_3d, axis=2))

# Mean along each axis
print("\nMean over axis=0:\n", np.mean(matrix_3d, axis=0))
print("\nMean over axis=1:\n", np.mean(matrix_3d, axis=1))
print("\nMean over axis=2:\n", np.mean(matrix_3d, axis=2))
