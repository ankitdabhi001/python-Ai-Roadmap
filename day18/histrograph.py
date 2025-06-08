import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from a normal distribution
data = np.random.randn(1000)

# Create histogram
plt.hist(data, bins=20, color='purple', edgecolor='black')
plt.title("📊 Histogram of Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.show()
