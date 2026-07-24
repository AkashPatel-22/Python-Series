# Data Cleaning.
# - Remove duplicates
# - Handle missing values
# - Remove outliers

# Handle missing values
# - Drop rows with missing value

# df.isnull() - shows True for missing values
# df.dropna(inplace=True)  # Drop rows with missing values
# df.fillna(value=0, inplace=True)  # Fill missing values with 0
# df.fillna(method='ffill', inplace=True)  # Forward fill missing values
# df.fillna(method='bfill', inplace=True)  # Backward fill missing values
# df.fillna(df.mean(), inplace=True)  # Fill missing values with mean of the column
# df.isnull().sum()  # Count of missing values in each column 

# Handle duplicates
# df.duplicated() - shows True for duplicate rows
# df.drop_duplicates(inplace=True)  # Drop duplicate rows

# Changing data types
# df.astype()  # Change data type of a column
# df.to_numeric()  # Convert column to numeric type
# df.to_datetime()  # Convert column to datetime type
# df.to_string()  # Convert DataFrame to string type