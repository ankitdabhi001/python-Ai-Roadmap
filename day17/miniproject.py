import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("ecommerce_sales_data.csv")
# print(df.head())

sorted=df.groupby("product")['sales'].mean()    
top_product=sorted.sort_values(ascending=False).head(3)

print("This Is Top 3 product By Sales : ")

print(top_product)

top_product.to_csv("top_product.csv")

# Monthly Trends

df['order_date']=pd.to_datetime(df['order_date'])

df['month']=df['order_date'].dt.to_period('M').astype(str)

monthly_sales=df.groupby('month')['sales'].sum().sort_index() # This is monthly trends
a=monthly_sales.sort_values(ascending=False).head(3)

print("Monthly Sales")
print(a)


order_counts = df['customer_id'].value_counts().head(3)
print("Most Active Customer :")
print(order_counts)

# Using Matplotlib Show The Chart

print("👥 Top 5 Most Active Customers (by number of orders):\n")



order_counts.plot(kind='bar',figsize=(10,5), title='Top 5 Active Customers', color='purple')
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()
