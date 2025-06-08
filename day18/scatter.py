import matplotlib.pyplot as plt
import numpy as np

# Generate dummy 2D data
x = np.random.rand(50) * 10    # 50 random X values (0 to 10)
y = np.random.rand(50) * 10    # 50 random Y values (0 to 10)

# Create scatter plot
plt.scatter(x, y, color='teal', marker='*')
plt.title("🔵 Scatter Plot of 2D Data Points")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.show()
