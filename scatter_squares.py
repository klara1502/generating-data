# Plotting and styling individual points with scatter()
"""
Sometimes it is useful to be able to plot and style individual
points based on certain characteristics
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

"""
A colormap is a series of colors in a gradient that moves from a starting
to an ending color
"""
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 4)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize = 14)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
