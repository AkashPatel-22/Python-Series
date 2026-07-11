# Operations On Arrays.
# -there are a lot of usefull operations that we can perform on our arrays.

import numpy as np
# 1. Reshaping.

arr = np.array([1,2,3,4,5,6])
print(arr.shape)

reshaped = arr.reshape((2,3)) # converts 1*6 -> 2*3
print(reshaped,reshaped.shape)

flattened = reshaped.flatten() # converts 2D => 1D
print(flattened,flattened.shape)



# 2. Slicing.

#  slicing 1D array
arr = np.array([1,2,3,4,5,6,7])

print(arr[2:6]) # 3,4,5,6
print(arr[:6]) # 1,2,3,4,5,6
print(arr[3:]) # 4,5,6,7
print(arr[::2]) # 3,4,5,6