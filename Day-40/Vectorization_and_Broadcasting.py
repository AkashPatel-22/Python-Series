#  Vectorization & Broadcasting
# - vectorization and broadcasting in numpy are two of the most powerfull features for fast numerical computations.

#  Vectorization.
# - vectorization means perfoming operations on entire arrays at once without explicit python loops.
# -- Numpy uses C-level implementations internally - much faster than python loops.
# -- makes code shorter, cleaner and faster.

import numpy as np

arr = np.array([1,2,3,4,5])

sq_arr = arr**2  # suare of all numbers
print(sq_arr)

arr2 = np.array([6,7,8,9,10])
print(arr + arr2)   # sum of two arrays