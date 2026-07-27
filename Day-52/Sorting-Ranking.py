# Sorting / Ranking

# 1. sort_values() - Sort a DataFrame by one or more columns
# 2. sort_index() - Sort a DataFrame by its index
# 3. rank() - Assign ranks to entries in a DataFrame based on their values

import pandas as pd

df = pd.DataFrame({'age': [25, 30, 22, 28],
                   'name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'score': [85, 90, 78, 92]})
print("Original DataFrame:",df)

df_sorted = df.sort_values(by='score', ascending=False)
print("Sorted DataFrame by score (descending):",df_sorted)

df_sorted_index = df.sort_index(ascending=True)
print("Sorted DataFrame by index (ascending):",df_sorted_index)