# Numpy Arrays Properties.
# - Array Properties- helps you understand and manipulate data in arrays efficiently.

# usefull attributes
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(arr.shape) # dimensions- (4*3)
print(arr.size) # total elementsv- (12)
print(arr.ndim) # no. of dimensions- 2
print(arr.dtype) # data type object- int64
print(arr.itemsize) # size of each elements in bytes - 8 for int 64