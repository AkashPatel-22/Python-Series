#  DataFrame.
# - a DataFrame is a two dimensional,tabular data structures (like a spreadsheet or SQL table).

#  It consits of:
# -- Rows
# -- Columns
# -- Index (row lables)
# -- Columns labels

# Each columns in DataFrame is a series

# usage.

import pandas as pd
# creating DataFrame in pandas -  using dictionary.
info = {
    "Name" : ["Adam","Eve","Bob"],
    "Marks" : [78,99,85],
    "Grade" : ['B','O','A']
}

df = pd.DataFrame(info)
print(df)
print(type(df))

print(df.index)   # row lables
print(df.columns)   # columns lables
