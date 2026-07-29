# Reshaping Methods.
# - We have three methods to reshape the data in pandas.  
#   1. reshape() - This method is used to change the shape of the data.
#   2. pivot() - This method is used to reshape the data by pivoting it around a column.
#   3. melt() - This method is used to reshape the data by unpivoting it from wide format to long format.

import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'foo', 'bar', 'baz'],
    'B': ['one', 'one', 'two', 'three', 'two', 'three'],
    'C': [1, 2, 3, 4, 5, 6],
    'D': [7, 8, 9, 10, 11, 12]
})

melted_df = pd.melt(df, id_vars=['A', 'B'], value_vars=['C', 'D'])  
print(melted_df)