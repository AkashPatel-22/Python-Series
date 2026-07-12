# Copy vs View.
# - slicing a list returns a copy but slicing a NumPy array returns a view - for efficiency.
# views is like a shallow copy that shares the same data as the original array, so no duplication happens here.

# -- views are fast and memory - efficient (no data duplication).
# --copies are safe but slower and use more memory.

# sliced list is a COPY.
import numpy as np

py_list = [1,2,3,4,5]
copy_list = py_list[1:4] # 2,3,4
copy_list[1] = 333
print(copy_list)
print(py_list) # 1,2,3,4,5 - remains same
print ("\n")

# sliced array is a VIEW.
np_arr = np.array([1,2,3,4,5])
view_arr = np_arr[1:4]  #2,3,4
view_arr[1] = 333
print(view_arr)
print(np_arr) # 1,2,333,4,5
print ("\n")


# creating a COPY for array

copy_arr = np_arr[1:4].copy()  # 2,3,4
copy_arr[2] = 444
print(copy_arr)
print(np_arr) # 1,2,3,4,5 - remain same