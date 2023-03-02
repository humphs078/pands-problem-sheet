# task_6_square_root.py
# Author: Sean Humphreys
# Script to return the square root of a number using Newton's method

# In numerical analysis, Newton's method, also known as the Newton–Raphson method, named after Isaac Newton and
# Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots
# (or zeroes) of a real-valued function - https://en.wikipedia.org/wiki/Newton%27s_method Last Accessed 02/03/2023

# Reference 1:
# https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx
# Last accessed 02/03/2023

# Reference 2:
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# Last accessed 02/03/2023


# define a function to calculate the square root of a floating point number using Newton's method
def newton_sqrt():
    # Declare variable to read in number by user as a string and cast to a floating point number
    number = float(input("Please enter a floating point number: "))
    # Declare variable for to crudely calculate a guess of the square root
    approx_root = number * .5
    # For loop to carry out Newton's calculation 100 times for accuracy. 100 is an arbitrary number.
    # If the range is too low the result will be crude or less precise. If too high more processing power will
    # be used and take longer to return a result
    for i in range(100):
        # variable describing the arithmetic for Newton's method
        better_approx = 0.5 * (approx_root + number / approx_root)
        # variable to use answer from previous calculation in the next iteration of the calculation
        approx_root = better_approx
    return better_approx


print(newton_sqrt())
