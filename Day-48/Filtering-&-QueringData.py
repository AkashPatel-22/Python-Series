# Filtering and Querying Data in Python

# 1.Boolean Filtering:
# - we can filter data based on conditions using boolean indexing.
# - We can filter a dataframe using a condition that returns a boolean Series.

# example:
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})   
filtered_df = df[df['A'] > 2]   
df[df['B'] < 7]
df[(df['A'] > 2) & (df['B'] < 8)]  # using multiple conditions with logical operators
print(filtered_df)


#  we can use  & for AND, | for OR, and ~ for NOT operations to combine multiple conditions.