# Renaming / Reordering

import pandas as pd

df = pd.DataFrame({
    'old_column_name': [1, 2, 3],
    'column1': [4, 5, 6],
    'column2': [7, 8, 9],
    'column3': [10, 11, 12]
})
print("Original DataFrame:",df)


# Renaming columns
df_renamed = df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)
print("Renamed DataFrame:")

# Reordering columns
df = df[['column3', 'column1', 'column2']]
print("Reordered DataFrame:",df)
