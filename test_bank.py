# bank.py
# Author: Sean Humphreys
# Script for adding cents and putting Euro - Task 2

# Import the Decimal method from the decimal library
from decimal import Decimal

# Variable for amount 1 in cents and covert to integer
amount_1 = Decimal(input("Enter amount 1 in (cent) "))

# Variable for amount 2 in cents and convert to integer
amount_2 = Decimal(input("Enter amount 2 (in cent) "))

# variable to define the sum of the 2 amounts output and convert to decimal
euro_total = (amount_1 + amount_2)/100
print(type(euro_total))

# line 15 of code was a problem as it prints €1.10 as €1.1 and not €1.10 as it
# print(f"The sum of these is €{c}")

# Fixes the issue encountered in my original line of code above e.g. €1.1 prints as €1.10. Cause of issue was
# formatting. Solution found @ Reference - http://programarcadegames.com/index.php?chapter=formatting&lang=en accessed
# 02/02/2023.


# Line 20 was original solution - newer format string used below. Changed on 02/03/2023
# Reference - https://java2blog.com/format-a-float-to-two-decimal-places/ accessed 02/03/2023
print(f"The total amount is €{euro_total}")
# print(f"The total amount is €{euro_total:.2f}")
