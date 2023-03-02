# task_2_bank.py
# Author: Sean Humphreys
# Script for adding cents and putting Euro - Task 2

# Variable for amount 1 in cents and covert to integer
a = int(input("Enter amount 1 in (cent) "))

# Variable for amount 2 in cents and convert to integer
b = int(input("Enter amount 2 (in cent) "))

# variable to define the sum of the 2 amounts output and convert to decimal
c = float((a + b)/100)

# line 15 of code was a problem as it prints €1.10 as €1.1 and not €1.10 as it
# print(f"The sum of these is €{c}")

# Fixes the issue encountered in my original line of code above e.g. €1.1 prints as €1.10. Cause of issue was
# formatting. Solution found @ Reference - http://programarcadegames.com/index.php?chapter=formatting&lang=en accessed
# 02/02/2023.
# print("The total amount is €""{:.2f}".format(c))

# Line 20 was original solution - newer format string used below. Changed on 02/03/2023
# Reference - https://java2blog.com/format-a-float-to-two-decimal-places/ accessed 02/03/2023
print(f"The total amount is €{c:.2f}")