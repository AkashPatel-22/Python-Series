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


# Selecting Rows:

# - we can select rows using the index or by using conditions.
# - By index labels .loc[]  - use row labels to select rows.
# - By index positions .iloc[]  - use row numbers to select rows.


df.loc[0]  # returns the first row as a Series
df.loc[0:1]  # returns the first two rows as a DataFrame
df.loc[0, "city"]  # returns the value in the first row and 'City' column

# NOTE : IN .loc[] When we slice,the end index is inclusive, meaning it includes the row at the end index.


df.iloc[1]  # returns the second row as a Series    
df.iloc[0:2]  # returns the first two rows as a DataFrame
df.iloc[0, 2]  # returns the value in the first row and third column

# NOTE : IN .iloc[] When we slice, the end index is exclusive, meaning it does not include the row at the end index.