# Multi- Dimensional Arrays.
# - multi-dimensional arrays in numpy are the foundation of most scientific and machine -learning work.
# - a numpy array can have any number of dimensions(1d,2d,3d & so on). Each dimension is called an axis.
# -- 1d arrays has 1 axix(axis0)
# -- 2d arrays has 2 axes (axix0 = row, axis1 = columns)
# -- 3d array has 3 axes (axis0 = depth/layer,axis1 = rows in each layer, axis2 = columns in each layer)

# 1D Array
import numpy as np
arr1D = np.array([1,2,3])
print(arr1D.ndim) # 1

# 2D Array (Matrix)
arr2D = np.array([[1,2,3],[4,5,6]])
print(arr2D.ndim) # 2

# 3D Array (Tensor)
arr3D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr3D.ndim) # 3