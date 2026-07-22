# Indexing & Data Selection

# Selecting Columns:
# - we can select a single column or multiple columns from a dataframe.

# example:
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)
# print("DataFrame:")
# print(df)

df['City']  # returns the 'City' column as a Series
df[['Name', 'Age']]  # returns a DataFrame with 'Name' and 'Age' columns