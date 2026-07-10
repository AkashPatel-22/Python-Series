# Creating Numpy Arrays
# - there are multiple ways of creating Numpy arrays,most common of which are:


# 1. From Python lists

# Creating Numpy Arrays - from lists

import numpy as np

arr = np.array([1,2,3,4])
print(arr,type(arr))

arr2 = np.array([1,2,3,4,"prime",3.14])
print(arr2,type(arr2))

# 2D Arrays -Matrix
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3,type(arr3))

# NOTE - ALL elements inn arr2 in above code will have same type (homogenous) unlike lists.
