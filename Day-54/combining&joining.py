# Combining and Joining DataFrames in Pandas

# In this tutorial, we will explore how to combine and join DataFrames in Pandas.
# We will cover various methods such as concatenation, merging, and joining.

# df.merge() 
# -is a powerful method that allows you to combine two DataFrames based on a common column or index.
# It is similar to SQL joins and can be used to perform inner, outer, left, and right joins.

# -Merge is used to combine two DataFrames based on a common column or index.
# It is similar to SQL joins and can be used to perform inner, outer, left, and right joins.


# it supports -
# Inner Join: Returns only the rows that have matching values in both DataFrames.
# Outer Join: Returns all rows from both DataFrames, with NaN in places where there are no matches.
# Left Join: Returns all rows from the left DataFrame and the matched rows from the right DataFrame. If there is no match, NaN is returned for the right DataFrame.
# Right Join: Returns all rows from the right DataFrame and the matched rows from the left DataFrame. If there is no match, NaN is returned for the left DataFrame. 
