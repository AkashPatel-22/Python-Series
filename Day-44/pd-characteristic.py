
#  Characteristics of a Series

# 1. they are homogeneous - store one type of data.
# 2. they support vectorized operations
# 3. they can handle missing values with NaN.
# 4. they have mutable values but immutable size.


#  Custom Indexing.
import pandas as pd

s2 = pd.Series([23,24,25,26],index = ["adam","eve","charlie","bob"])
print(s2["eve"])   # 24
print(s2["bob"])   # 26
print("\n")

#  Vectorized Operations
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
print(s1 + s2)
print("\n")

#  Mutable Values but immutable size.

s = pd.Series([1,2,3,4,5])
s[0] = 100

print(s)
changed_s = s.drop(1)
print(changed_s)
print(s)