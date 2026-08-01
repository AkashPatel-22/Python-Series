# Combining and Joining DataFrames in Pandas

# We will cover various methods such as concatenation, merging, and joining.

# df.merge() 
# -is a powerful method that allows you to combine two DataFrames based on a common column or index.
# It is similar to SQL joins and can be used to perform inner, outer, left, and right joins.

# -Merge is used to combine two DataFrames based on a common column or index.
# It is similar to SQL joins and can be used to perform inner, outer, left, and right joins.


# it supports Multiple joins -

# Inner Join: Returns only the rows that have matching values in both DataFrames.
# Outer Join: Returns all rows from both DataFrames, with NaN in places where there are no matches.
# Left Join: Returns all rows from the left DataFrame and the matched rows from the right DataFrame. If there is no match, NaN is returned for the right DataFrame.
# Right Join: Returns all rows from the right DataFrame and the matched rows from the left DataFrame. If there is no match, NaN is returned for the left DataFrame. 


#  Merging & Joining.

import pandas as pd
df1 = pd.DataFrame({
     'key': ['A', 'B', 'C', 'D'],   
     'value1': [1, 2, 3, 4]
 }) 

df2 = pd.DataFrame({
     'key': ['B', 'D', 'E', 'F'],
     'value2': [5, 6, 7, 8]
 }) 

pd.merge(df1, df2, on='key', how='inner')  # Inner Join 
pd.merge(df1, df2, on='key', how='outer')  # Outer Join
pd.merge(df1, df2, on='key', how='left')   # Left Join
pd.merge(df1, df2, on='key', how='right')  # Right Join 

# df.concat()
# -is used to concatenate two or more DataFrames along a particular axis (row-wise or column-wise).
# It can be used to combine DataFrames with the same columns or different columns.  

pd.concat([df1, df2], axis=0)  # Concatenate along rows
pd.concat([df1, df2], axis=1)  # Concatenate along columns
pd.concat([df1, df2], axis=0, ignore_index=True)  # Concatenate along rows and reset index  
