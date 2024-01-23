import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
file_path = 'Test_knight.csv'
df = pd.read_csv(file_path)

# Get the column names
columns = df.columns

# Create a histogram for each column
fig, axes = plt.subplots(nrows=6, ncols=5, figsize=(15, 15), tight_layout=True)

# Flatten the 2D array of axes into a 1D array
axes = axes.flatten()

for i, column in enumerate(columns):
    ax = axes[i]
    ax.hist(df[column], bins=50, color='limegreen', edgecolor='none')
    ax.set_title(column)
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.legend(['Knight'], loc='upper right')

# Adjust layout
plt.show()
