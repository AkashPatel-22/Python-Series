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


# Broadcasting
# - allows numpy to automatically expand arrays of different shapes so that arithmetic operations can be performed.
# - it is basically scaling arryas without using extra money
# -- no neend to manually re shape arrays.
# -- usefull for combining arrays of different dimensions.

# Broadcasting Rule.
# - Broadcasting can only take place when the arrays are of compatible shape.so numpy compares shapes of arrays
#  FROM RIGHT TO LEFT . for the array to be compatible, all dimensions must either be:
# -- equal or
# -- 1, or
# -- missing (smaller arrays can be "stretched")


# Broadcasting with a Scaler.
import numpy as np

arr_mul10 = arr * 10  # multiply by 10 to all numbers
print(arr_mul10)

#  Broadcasting with a vector
arr1d = np.array([1,2,3])
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr1d+arr2d)


#  A quite common example of broadcasting in vector normalization.
# this is very common in machine learning and data preprocessing.