import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

# Show first 5 rows
print("📊 Preview:")
print(df.head(5))

# Clean Data
df.dropna(inplace=True)

# Analysis: Total sales per region and product
sales_by_region = df.groupby("product")['sales'].sum()

print("\n💰 Total Sales by Region:")
print(sales_by_region)

# save and conver to csv
sales_by_region.to_csv("product.csv")