# DataFrame Methods in Pandas.

# - we have a lot of useful methods with dataframe.

# Data Viewing and Inspection:
# - these help us take a quick look at our datasets.

# 1. df.head(n) - shows first n rows (default=5)
# 2. df.tail(n) - shows last n rows (default=5)

# 3. df.sample(n) - shows random n rows (deafult=1)
# 4. df.info() - Displays column names, datatypes, memory usage.

# 5. df.describe(n) - shows descriptive statistics for numeric columns

#  we also have attributes like :

# 1. df.shape - returns the dimensions of the dataframe (rows, columns)
# 2. df.columns - returns the column names
# 3. df.dtypes - returns the data types of each column


import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print(df.head(2))  # Display first 2 rows
print(df.tail(1))  # Display last row   
print(df.sample(2))  # Display 2 random rows
print(df.info())  # Display dataframe information
print(df.describe())  # Display descriptive statistics
print(df.shape)  # Display dimensions
print(df.columns)  # Display column names
print(df.dtypes)  # Display data types