import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Sum of rows
row_sums = np.sum(matrix, axis=1)
print("Row sums using NumPy:", row_sums)

# Sum of columns
col_sums = np.sum(matrix, axis=0)
print("Column sums using NumPy:", col_sums)





matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Sum of rows
row_sums = []
for row in matrix2:
    total = 0
    for val in row:
        total += val
    row_sums.append(total)
print("Row sums (custom logic):", row_sums)

# Sum of columns
col_sums = []
num_cols = len(matrix2[0])
for col in range(num_cols):
    total = 0
    for row in matrix2:
        total += row[col]
    col_sums.append(total)
print("Column sums (custom logic):", col_sums)
