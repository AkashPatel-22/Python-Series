# 3.Indexing.

import numpy as np

# indexing for 1d array.
arr = np.array([1,2,3,4,5])
print(arr[1])

# indexing for 2d array.
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) # 2d array
print(arr[0][1]) #2  r * c
print(arr[1][2]) #6  r * c



# Fancy indexing- means accessing array elements using integer array/lists of indices rather than plain slices (:).
# fancy Indexing.
arr = np.array([1,2,3,4,5])
idx = [0,1,4]
print(arr[idx]) # print nums at given indices
print("\n")


# Boolean masking(or indexing) - means using a boolean array (true/false) to select elements from another array.

#  boolean indexing

print(arr[arr>2])  # print nums greater than 2
print(arr[arr % 2 == 0 ]) #print even num