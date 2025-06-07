import pandas as pd

# Load Excel file (make sure the file is in your directory)
df = pd.read_excel("data.xlsx")  # You can also use .xls or .csv

# Loop through each row
for index, row in df.iterrows():
    print(f"Row {index + 1}: Name={row['Name']}, Age={row['Age']}")
