# accounts.py
# Author: Sean Humphreys
# Script to read in a bank account no', display only the last 4 digits and mask the rest

# variable to input bank account no
account_no = str(input("Please enter a 10 digit bank account number: "))

# command to print mask 1st six digits and only print the last 4 digits
print(f"xxxxxx{account_no[-4:]}")