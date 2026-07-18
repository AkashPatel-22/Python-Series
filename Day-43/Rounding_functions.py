# Rounding functions in Python
# - Numpy provides a wide range of built-in rounding functions that are highly optimized and can operate on element-wise on arrays.

# 1.around() : rounds an array to the given number of decimals.
# 2.floor() : rounds an array down to the nearest integer.
# 3.ceil() : rounds an array up to the nearest integer.
# 4.trunc() : rounds an array towards zero.

import numpy as np
array = np.array([1.5, 2.3, 3.7, 4.1, 5.9])
print("Original Array:", array)

print("Rounded Array:", np.around(array))
print("Floor Array:", np.floor(array))

print("Ceil Array:", np.ceil(array))
print("Trunc Array:", np.trunc(array))