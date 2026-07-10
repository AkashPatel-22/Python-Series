# 2. Using built-in functions

#  Creating Numpy Arrays - from scratch
import numpy as np

# 3*4 arrays of 0s.
arr1 = np.zeros((3,4))
print(arr1, arr1.shape)
print("\n")

arr2 = np.ones((3,3)) # 3*3 array of 1s
print(arr2, arr2.shape)
print("\n")

arr3 = np.full((2,3),5) #2*3 arrays of 5s
print(arr3, arr3.shape)
print("\n")

arr4 = np.eye(3) # Identity matrix of 3*3
print(arr4, arr4.shape)
