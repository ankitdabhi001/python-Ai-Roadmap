import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take user input for 7 days
temperatures = []
print("📥 Enter temperatures for 7 days:")

for i in range(1, 8):
    temp = float(input(f"Day {i} temperature (°C): "))
    temperatures.append(temp)

# Step 2: Convert to NumPy array
temps_array = np.array(temperatures)

# Step 3: Process data
mean_temp = np.mean(temps_array)
max_temp = np.max(temps_array)
min_temp = np.min(temps_array)

# Step 4: Print summary
print("\n📊 Weather Summary:")
print(f"Average Temperature: {mean_temp:.2f} °C")
print(f"Maximum Temperature: {max_temp} °C")
print(f"Minimum Temperature: {min_temp} °C")

# Step 5: Visualize using Matplotlib
days = np.arange(1, 8)
plt.plot(days, temps_array, marker='o', linestyle='-', color='skyblue', label='Temp')
plt.axhline(mean_temp, color='orange', linestyle='--', label='Mean Temp')
plt.title("🌦️ Weekly Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
