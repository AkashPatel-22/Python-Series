# Transforming Data.

# apply() - Apply a function to each element of a column
# df['column_name'].apply(function)  # Apply a function to a column 

# map() - Map values of a column to another set of values
# df['column_name'].map({'old_value1': 'new_value1', 'old_value2': 'new_value2'})  # Map values of a column to another set of values

# replace() - Replace values in a column
# df['column_name'].replace({'old_value1': 'new_value1', 'old_value2': 'new_value2'}, inplace=True)  # Replace values in a column

# fillna() - Fill missing values in a column
# df['column_name'].fillna(value='new_value', inplace=True)  # Fill missing values in a column with a specific value

# astype() - Change data type of a column
# df['column_name'] = df['column_name'].astype('new_data_type')

# rename() - Rename columns in a DataFrame
# df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)  #

# assign() - Assign new columns to a DataFrame
# df.assign(new_column_name=df['column_name'] * 2)  # Assign a new column to a DataFrame

