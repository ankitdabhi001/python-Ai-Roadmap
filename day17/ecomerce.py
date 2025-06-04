import pandas as pd

df=pd.read_csv("ecommerce_sales_data.csv")
# print(df.head())

sorted=df.groupby("product")['sales'].sum()
top_product=sorted.sort_values(ascending=False).head(3)

print("This Is Top 5 product By Sales ")
print(top_product)

top_product.to_csv("top_product.csv")