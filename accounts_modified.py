# accounts.py
# Author: Sean Humphreys
# Script to read in a bank account number display only the last 4 digits and mask the rest

# - the term mask in the commentary below refers to the portion of the account no to be hidden
# by the character "x"

# Assumptions:
# - the last 4 digits will always be displayed regardless of the account number length
# - if an account number is 4 digits or fewer in length, by definition applying the
#  above assumption it cannot be masked
# - the account number can only contain numbers. It cannot contain letters.
# - loop statements and the use of if and else statements are permitted in the script.


# Reference - https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input
# above page last accessed 11/02/2023 - describes how to use a loop

# declare a Boolean variable
valid_input = False

# define while loop e.g. while the valid_input variable is True do the following
while not valid_input:
    ac_no = input("Please enter an account number: ")  # declare variable to capture input of statement string
    ac_no_len = len(ac_no)  # declare variable for account no length
    ac_no_mask = ac_no_len - 4  # declare variable for the length of the required mask
    mask = ac_no_mask * "x"  # variable to define the mask to precede the last 4 digits of the
    # account number
    masked_ac_no = mask + ac_no[-4:]  # variable to define the masked account number
    if ac_no.isnumeric() is True and len(ac_no) > 4:  # if the account number input contains only numbers
        # and is greater than 4 characters do the following
        print(masked_ac_no)  # print statement to print the ac_no variable last 4 digits and mask the rest
        valid_input = True  # declare the valid_input variable to be true therefore the code stops
    elif len(ac_no) <= 4 and ac_no.isnumeric() is True:  # if the account number is less than 4 digits print the
        # message in line 37
        print(f"{masked_ac_no}\nIt is not possible to mask account numbers shorter than 5 digits long.")
        valid_input = True  # close the loop
    else:  # else state - otherwise do this e.g. if the valid_input variable is false
        print("That is not a valid account number. Account numbers cannot contain letters")  # print this and loop
        # back to line 23
