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