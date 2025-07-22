import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate random float dataset of shape (5, 4) with values between 0 and 100
data = np.random.uniform(low=0.0, high=100.0, size=(5, 4))

print("Original Data:\n", data)

# Min-Max Normalization
min_val = np.min(data)
max_val = np.max(data)

normalized_data = (data - min_val) / (max_val - min_val)

print("\nNormalized Data (0 to 1):\n", normalized_data)
