# Task_4_collatz.py
# Author: Sean Humphreys
# Script to read in a positive integer and print the collatz sequence for that number
# used to create while loop to ensure only a positive integer can be read in

# Reference 1 - https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input
# above page last accessed 11/02/2023 - used for loop in line 20 of code so only a positive integer
# can be read in by the user

# Reference 2: https://hackernoon.com/implementing-3x1-in-python Accessed 18/02/2023
# used in line 24 to create while loop to iterate list containing the Collatz sequence

# Reference 3: https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# Accessed 18/02/2023. Used in line 30 of script to print list without brackets or commas

# Reference 4:  https://stackoverflow.com/questions/25733737/how-to-print-out-a-string-and-list-in-one-line-python
# accessed 18/02/2023 - used for print statement in line 33 of script

valid_input = False
while not valid_input:
    num = int(input("Please enter a positive integer: "))
    if num == 1:
        print(f"The Collatz sequence for {num} is 4 2 1 ")
        break
    else:
        if num > 0:
            sequence = [num]
            while (num != 1):
                if ((num % 2) == 0):
                    num = num // 2
                else:
                    num = (num * 3) + 1
                sequence.append(num)
            print(f"The collatz sequence for {sequence[0]} is", *sequence[1:], sep=" ")
            valid_input = True
        else:
            print(f"{num} is not a positive integer.")