# Log & Exponential Functions in Python

# 1.log() : returns the natural logarithm of array elements.
# 2.log10() : returns the base-10 logarithm of array elements.  
# 3.log2() : returns the base-2 logarithm of array elements.
# 4.exp() : returns the exponential of array elements.

import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("Original Array:", array)
print("Natural Logarithm:", np.log(array))
print("Base-10 Logarithm:", np.log10(array))
print("Base-2 Logarithm:", np.log2(array))
print("Exponential:", np.exp(array))