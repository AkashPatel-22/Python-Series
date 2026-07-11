# We can also explicitly change the dtype for our arrays.

# specify dtype at creation
import numpy as np

str_arr = np.array([1,2,3,4], dtype="U")
print(str_arr,str_arr.dtype)

float_arr = np.array([1,2,3,4], dtype="float64")
print(float_arr,float_arr.dtype)


# creating new array with a specific type from existing array
int_arr = float_arr.astype(np.int64)
print(int_arr,int_arr.dtype)

