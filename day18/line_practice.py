import numpy as np
import matplotlib.pyplot as plt

# Generate dummy data
days = np.arange(1, 8)
temperature = np.array([22, 24, 19, 21, 25, 23, 20])

# Plotting
plt.plot(days, temperature, marker='D', linestyle='-', color='blue') # use for show the grid line graph 
# plt.bar(days,temperature,color='green')  # use for graph in the blocks
plt.title("📈 Weekly Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
