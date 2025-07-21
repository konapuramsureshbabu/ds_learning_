import numpy as np
import random

# Generate a random 1D array of 10 integers between 0 and 100
arr = np.random.randint(0, 100, size=10)

# Find min and max
min_val = np.min(arr)
max_val = np.max(arr)

print("Random Array:", arr)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)


# Generate random array of 10 integers between 0 and 100
arr = [random.randint(0, 100) for _ in range(10)]

# Find min and max
min_val = min(arr)
max_val = max(arr)

print("Random Array:", arr)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)
