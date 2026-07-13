# Operations on 3D Arrays

import numpy as np

arr3D = np.array([[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]])
print(arr3D,arr3D.shape)
print("\n")

# indexing
print(arr3D[0][1][1])  # 4
print(arr3D[0][5][1])  # 12
print("\n")

print(arr3D[:,:,0])  # first columns from both layers
print(arr3D[:,0,:])  # first rows from both layers
print("\n")


# manipulating data

arr3D[:,0,:] = 99 # changing first row to store 99
print(arr3D)
