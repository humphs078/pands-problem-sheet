# task_7_plottask.py
# Author: Sean Humphreys
# Script called plottask.py that displays:
# a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2,
# and a plot of the function  h(x)=x3 in the range [0, 10],
# on the one set of axes.
import numpy as np  # import the numpy module as np
from numpy import random  # from the numpy package import the random module
import matplotlib.pyplot as plt  # import the matplotlib.pyplot as plt

x_axis_list = []  # variable with empty list to be populated with values for the x-axis
np.random.seed(10)  # seed so as the random numbers do not change on each run of the script

# declare a variable to randomly generate 1000 values with a mean of 5 and SD of 2
random_numbers = random.normal(loc=5, scale=2, size=1000)


# define a function to plot of the function  h(x)=x3 in the range [0, 10]
def plot_func():
    list_y_axis = []  # variable wit empty list
    for z in range(0, 10):  # for loop for desired range of values
        y = z * z * z  # arithmetic to cube y
        list_y_axis.append(y)  # append y to list
    return list_y_axis  # return the list of values that will be used in the y-axis


for x in range(0, 10):  # for loop to create a list of values for the x-axis
    x_axis_list.append(x)  # append the desired values in a list for the x-axis
# Define a dictionary with key value pairs
font1 = {'family': 'serif', 'color': '#6495ED', 'size': 20}
font2 = {'family': 'serif', 'color': '#9932CC', 'size': 10}
x_axis = np.array(x_axis_list)
y_axis = np.array(plot_func())
plt.hist(random_numbers, color="#A9A9A9")
plt.plot(x_axis, y_axis, color='#006400', linewidth='2')
plt.grid(color='#8A2BE2', linewidth="0.1")
plt.title("Week 8 Task - plottask.py", fontdict=font1)
plt.xlabel("Number", fontdict=font2)
plt.ylabel("Number Cube", fontdict=font2)
plt.show()
