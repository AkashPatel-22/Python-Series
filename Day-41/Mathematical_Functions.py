# Mathematical Functions in Python
# - Numpy is massive and provides a wide range of built-in mathematical functions that are highly optimized
# and can operate on element-wise on arrays. let's have a look at some of them.


# aggregate functions
# - sum() : returns the sum of array elements over a given axis.
# - mean() : returns the average of array elements over a given axis.
# - std() : returns the standard deviation of array elements over a given axis.
# - var() : returns the variance of array elements over a given axis.   
# - min() : returns the minimum value of array elements over a given axis.
# - max() : returns the maximum value of array elements over a given axis.
# - median() : returns the median of array elements over a given axis.
# - prod() : returns the product of array elements over a given axis.

import numpy as np
array = np.array([1, 2, 3, 4, 5])

print("Sum:", np.sum(array))
print("Mean:", np.mean(array))
print("Standard Deviation:", np.std(array))

print("Variance:", np.var(array))
print("Minimum:", np.min(array))