# A number raised to the third power is a cube.
# Plot the first five cubic numbers, and then plot the first 5000 cubic numbers

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 40)

plt.title("Cubic Numbers", fontsize = 14)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Cubic of Numbers", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
