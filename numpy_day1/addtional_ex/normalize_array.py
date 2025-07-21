import numpy as np

# Sample array
data = np.array([10, 20, 30, 40, 50])

# Min-Max Normalization
min_val = np.min(data)
max_val = np.max(data)
normalized = (data - min_val) / (max_val - min_val)

print("Original data:", data)
print("Normalized data (0 to 1):", normalized)

#custom logic for normalization
data2 = [10, 20, 30, 40, 50]

min_val = min(data2)
max_val = max(data2)

normalized = [(x - min_val) / (max_val - min_val) for x in data2]

print("Original data:", data2)
print("Normalized data (0 to 1):", normalized)
