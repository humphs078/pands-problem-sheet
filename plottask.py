# plottask.py
# Author: Sean Humphreys
# Script called plottask.py that displays:
# a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2,
# and a plot of the function  h(x)=x3 in the range [0, 10],
# on the one set of axes.
# Reference 1: https://www.w3schools.com/python/numpy/numpy_random_normal.asp last accessed 16/03/2023
# Reference 2: https://www.w3schools.com/python/matplotlib_intro.asp last accessed 16/03/2023
# Reference 3: https://www.w3schools.com/python/matplotlib_labels.asp last accessed 16/03/2023
# Reference 4: https://www.w3schools.com/colors/colors_names.asp last accessed 16/03/2023
# Reference 5: https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/ last accessed 23/03/2023

import numpy as np  # import the numpy module as np
from numpy import random  # from the numpy package import the random module
import matplotlib.pyplot as plt  # import the matplotlib.pyplot as plt

x_axis_list = []  # variable with empty list to be populated with values for the x-axis
np.random.seed(10)  # seed so as the random numbers do not change on each run of the script
mean = 5  # variable for mean value
standard_deviation = 2  # variable for standard deviation
no_of_values = 1000  # variable for number of values to be generated
# declare a variable to randomly generate 1000 values with a mean of 5 and SD of 2
random_numbers = random.normal(loc=mean, scale=standard_deviation, size=no_of_values)


# define a function to plot of the function  h(x)=x3 in the range [0, 10]
def plot_func():
    list_y_axis = []  # variable wit empty list
    for z in range(0, 10):  # for loop for desired range of values
        y = z * z * z  # arithmetic to cube y
        list_y_axis.append(y)  # append y to list
    return list_y_axis  # return the list of values that will be used in the y-axis


for x in range(0, 10):  # for loop to create a list of values for the x-axis
    x_axis_list.append(x)  # append the desired values in a list for the x-axis
# Define a dictionary with key value pairs for font formatting
font1 = {'family': 'serif', 'color': '#6495ED', 'size': 20}
# Define a dictionary with key value pairs for font formatting
font2 = {'family': 'serif', 'color': '#9932CC', 'size': 10}
x_axis = np.array(x_axis_list)  # variable with array for x-axis
y_axis = np.array(plot_func())  # variable with array for y-axis
plt.hist(random_numbers, color="#A9A9A9")  # plot histogram with black colour
plt.plot(x_axis, y_axis, color='#006400', linewidth='2')  # plot line with green colour and width 2
plt.grid(color='#8A2BE2', linewidth="0.1")  # plot a black light blue with line width 0.1
plt.title("Week 8 Task - plottask.py", fontdict=font1)  # display title with font 1 formatting
plt.xlabel("X Number", fontdict=font2)  # display x-axis label with font 2 formatting
plt.ylabel("Frequency / X Number Cube", fontdict=font2)  # display y-axis with font 2 formatting
plt.legend(["h(x)=x^3", "Distribution (mean of 5 and SD of 2)"], loc="upper left")  # display legend in the upper
# left corner
plt.show()  # command to show plot
