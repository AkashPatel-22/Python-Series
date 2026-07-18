# Miscellaneous Functions in Python

# 1. abs() : returns the absolute value of array elements.
# 2. sign() : returns the sign of array elements.
# 3. clip() : clips (limits) the values in an array.
# 4. unique() : finds the unique elements of an array.
# 5. sort() : sorts the elements of an array in ascending order.

import numpy as np
array = np.array([-1, -2, 3, 4, -5])

print("Original Array:", array)
print("Absolute Value:", np.abs(array))
print("Sign of Elements:", np.sign(array))
print("Clipped Array:", np.clip(array, -3, 3))
print("Unique Elements:", np.unique(array))
print("Sorted Array:", np.sort(array))