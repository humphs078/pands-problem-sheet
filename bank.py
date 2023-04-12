# bank.py
# Author: Sean Humphreys
# Script for adding cents and putting Euro - Task 2

# Import the Decimal method from the decimal library. This library is specifically for working with currency and
# eliminates the problem of representing base 10 floating point numbers as base 2
# https://learnpython.com/blog/count-money-python/ - last accessed 12/04/2023
# https://docs.python.org/3/library/decimal.html - last accessed 12/04/2023
from decimal import Decimal

# Variable for amount 1 in cents and convert to Decimal class
amount_1 = Decimal(input("Enter amount 1 in (cent) "))

# Variable for amount 2 in cents and convert to Decimal class
amount_2 = Decimal(input("Enter amount 2 (in cent) "))

# variable to define the sum of the 2 amounts output and convert to euro.cents
euro_total = (amount_1 + amount_2)/100

# validation statement to check the class of the euro_total variable, commented out but left in to demonstrate that a
# check was performed to confirm the absense of floats
# print(type(euro_total))

# Final print statement, formatting a string
print(f"The total amount is €{euro_total}")
