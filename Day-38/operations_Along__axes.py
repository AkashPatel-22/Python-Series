# Operations Along Axes
# - we can also perform certain operations along a specific axis in an array.

import numpy as np
arr2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr2D))  # sum of entire array - 45

sum_of_columns = np.sum(arr2D,axis = 0)
print(sum_of_columns) # 12,15,18

sum_of_rows = np.sum(arr2D,axis = 1)
print(sum_of_rows)  # 6,15,24

# slicing 
print(arr2D[0:3,1:3]) # slice rows (0,1,2) x cols (1,2)