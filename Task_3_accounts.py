# Task_3_accounts.py
# Author: Sean Humphreys
# Script to read in a bank account number display only the last 4 digits and mask the rest

# Assumptions:
# - the account number has to be 10 numbers. It cannot be greater or less than 10 numbers in length.
# - the account number can only contain numbers. It cannot contain letters.

# variable to input bank account no and convert to integer. If it is not an integer letters
# can be entered into the account number
account_no = int(input("Please enter a 10 digit bank account number: "))

# variable to convert account number to a string to measure the length of the account number
account_no_length = str(account_no)

# if statement to print the account number with the first 6 digits masked as x if the account no is 10
# digits long
if len(account_no_length) == 10:
    print(f"xxxxxx{account_no_length[-4:]}")

# elif statement to ask for correct account no' length the account no' is longer than 10 numbers
elif len(account_no_length) > 10:
    print(f"The account number you have entered is longer than 10 characters. Please enter a valid account number.")

# elif statement to ask for correct account no' length if the account no' is less than 10 numbers
elif len(account_no_length) < 10:
    print(f"The account number you have entered is less than 10 numbers. Please enter a valid account number.")
