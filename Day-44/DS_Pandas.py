# #  Core Data Structure in Pandas.

# Series.

# -a Series is a one-dimensional labeled array (like a column in a spreadsheet).
# it can hold data of any type: int, float, str, python objects.

# -- It has two main components.
# 1. values - the actual data.
# 2. index - labels for each value.

import pandas as pd

s = pd.Series([23,24,25,26])
print(s)
print(type(s))

# indexing.
print(s[0])  # 23
print(s[2])  # 25
print(s.index)  # all lebels
