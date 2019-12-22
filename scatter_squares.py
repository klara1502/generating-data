# Plotting and styling individual points with scatter()
"""
Sometimes it is useful to be able to plot and style individual
points based on certain characteristics
"""

import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize = 14)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
