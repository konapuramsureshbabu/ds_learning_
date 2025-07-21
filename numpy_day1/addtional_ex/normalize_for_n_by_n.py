import numpy as np

# Sample n x n matrix
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Min-Max Normalization
min_val = np.min(matrix)
max_val = np.max(matrix)

normalized_matrix = (matrix - min_val) / (max_val - min_val)

print("Original Matrix:\n", matrix)
print("\nNormalized Matrix (0 to 1):\n", normalized_matrix)


# Sample n x n matrix
matrix2 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Flatten matrix to find global min and max
flat = [val for row in matrix2 for val in row]
min_val = min(flat)
max_val = max(flat)

# Normalize each element
normalized_matrix = []
for row in matrix2:
    normalized_row = [(x - min_val) / (max_val - min_val) for x in row]
    normalized_matrix.append(normalized_row)

print("Original Matrix:")
for row in matrix2:
    print(row)

print("\nNormalized Matrix (0 to 1):")
for row in normalized_matrix:
    print(["{:.2f}".format(x) for x in row])
