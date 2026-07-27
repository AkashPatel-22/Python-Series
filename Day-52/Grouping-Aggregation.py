# Grouping / Aggregation

# - groupby() - Split a DataFrame into groups based on some criteria
# - aggregate() - Compute summary statistics for each group

import pandas as pd

df = pd.DataFrame({'category': ['A', 'B', 'A', 'B', 'A'],
                   'value': [10, 20, 30, 40, 50]})
print("Original DataFrame:",df)

grouped = df.groupby('category')
print("Grouped DataFrame:",grouped)

df_aggregated = grouped.aggregate({'value': 'sum'})
print("Aggregated DataFrame (sum of values by category):",df_aggregated)

# Aggregate multiple functions
# df.sum(),
# df.mean(),
# df.max()
# can be used to aggregate multiple functions on the grouped data

df_aggregated_multiple = grouped.aggregate({'value': ['sum', 'mean', 'max']})
print("Aggregated DataFrame (sum, mean, max of values by category):",df_aggregated_multiple)