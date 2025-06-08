import matplotlib.pyplot as plt

# Product names and their sales
products = ['Product A', 'Product B', 'Product C']
sales = [150, 230, 180]

# Create bar chart
plt.bar(products, sales, color=['green', 'blue', 'orange'])
plt.title(" Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show plot
plt.show()
