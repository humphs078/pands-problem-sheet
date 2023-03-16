# accounts.py
# Author: Sean Humphreys
# Script to read in a bank account number display only the last 4 digits and mask the rest

# Assumptions:
# - the account number has to be 10 numbers. It cannot be greater or less than 10 numbers in length.
# - the account number can only contain numbers. It cannot contain letters.
# - loop statements and the use of if and else statements are permitted in the script.

# Reference - https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input
# above page last accessed 11/02/2023 - describes how to use a loop

# declare a Boolean variable
valid_input = False

# define while loop e.g. while the valid_input variable is True do the following
while not valid_input:
    print("Please enter a 10 digit account number: ")  # print statement
    ac_no = input()  # declare variable to capture input of statement above
    if len(ac_no) == 10 and ac_no.isnumeric() is True:  # if the length of the string is = 10 and the contents
        # numeric do the following
        print(f"xxxxxx{ac_no[-4:]}")  # print statement to print the ac_no variable last 4 digits
        valid_input = True  # declare the valid_input variable to be true therefore the code stops
    else:  # else state - otherwise do this e.g. if the valid_input variable is false
        print("That is not a valid 10 digit account number.\nAccount numbers cannot contain letters or be less than 10 digits long")  # print this and loop back to line 17
