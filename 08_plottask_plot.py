# This script generates a plot for the function y = h(x) = x^3

# References: 
# Lecture 8.2 for Programming and Scripting
# https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
# https://www.educative.io/answers/what-is-the-matplotlibpyplotsavefig-function-in-python
# https://www.geeksforgeeks.org/matplotlib-pyplot-ylabel-in-python/
# https://www.geeksforgeeks.org/style-plots-using-matplotlib/?ref=lbp



# These two commands import the NumPy and Matplotlib libraries respectively, which are needed to create the plot.
import numpy as np
import matplotlib.pyplot as plt

# This imports the 'style' module, which enables the user to enhance the appearance of the plots they
# create, by imposing built-in or customised style packages onto them.
from matplotlib import style

# This imposes a specific built-in style package to the plot.
plt.style.use('Solarize_Light2') 

# These generate the x and y coordinates, respectively, on the plot.
xpoints = np.array(range(1,10))
ypoints = xpoints*xpoints*xpoints

# These print on to the plot the title, x-axis label, y-axis label and the content (and position - default set to top left) of 
# the legend for the plot.
plt.title("week 8 - plot")
plt.xlabel("x")
plt.ylabel("h(x)")

# This generates the plot, creates a legend in the top-left corner and selects the colour of the plot.
plt.plot(xpoints, ypoints, label = "x cubed", color = "orange")
plt.legend()

# This prints out the plot.
plt.show()