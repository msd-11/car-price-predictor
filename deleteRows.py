import pandas as pd

# Read the csv file
data = pd.read_csv('vehicles2.csv')

# Remove rows that contain an empty value in any column
data = data.dropna()

# Save the cleaned data to a new csv file
data.to_csv('cleaned_data.csv', index=False)
