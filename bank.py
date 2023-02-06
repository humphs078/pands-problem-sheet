# bank.py
# Author: Sean Humphreys
# Script for adding cents and putting Euro - Task 2

a = int(input("Enter the first amount in cents ")) # Variable for amount 1 in cents and covert to integer

b = int(input("Enter the second amount in cents ")) # Variable for amount 2 in cents and convert to integer

c = float((a + b)/100) # variable to define the sum of the 2 amounts output and convert to decimal

# print(f"The total amount is €{c}") # my original line of code was a problem as it prints €1.10 as €1.1 and not €1.10 as it should be

print("The total amount is €""{:.2f}".format(c)) # Reference - http://programarcadegames.com/index.php?chapter=formatting&lang=en accessed 02/02/2023
