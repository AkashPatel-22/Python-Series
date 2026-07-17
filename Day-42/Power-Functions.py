# Power Functions in Python
# - Numpy provides a wide range of built-in power functions that are highly optimized and can operate on element-wise on arrays. 
# let's have a look at some of them.

# 1.square() : returns the square of array elements.
# 2.sqrt() : returns the square root of array elements.
# 3.cbrt() : returns the cube root of array elements.

import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("Square:", np.square(array))
print("Square Root:", np.sqrt(array))
print("Cube Root:", np.cbrt(array))