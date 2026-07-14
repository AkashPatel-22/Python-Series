# Data Types.
#  - We have already discussed how every Numpy array has a single data type.
# (homogeneous arrays) and it is stored in the .dtype attribute.

# - the most common data types in NumPy
# 1. Integer literals : int32,int64
# 2. floating literals : float32,float64
# 3. Boolean : bool
# 4. Complex numbers : complex64, complex128
# 5. String : s(byte-str)& u (unicode-str)
# 6. Object : generic python objects - object


# Common Data Types.
import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = np.array([1.0,2.0,3.0])
arr3 = np.array(["hello","world","of","prime"])
print(arr.dtype) # int64
print(arr2.dtype) # float64
print(arr3.dtype) #U


# Complex Numbers.
arr1 = np.array([2+3j])
arr2 = np.array([5+7j])

print(arr1,arr1.dtype)
print(arr1 + arr2)
print(arr1 - arr2)


# Objects.
arr = np.array(["hello",{1,2,3},3.14])
print(arr,arr.dtype)