# task_4_collatz.py
# Author: Sean Humphreys
# Script to read in a positive integer and print the collatz sequence for that number
# used to create while loop to ensure only a positive integer can be read in

# Reference 1 - https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input
# above page last accessed 11/02/2023 - used for loop in line 20 of code so only a positive integer
# can be read in by the user

# Reference 2: https://hackernoon.com/implementing-3x1-in-python Accessed 18/02/2023
# used in line 28 to create while loop to iterate list containing the Collatz sequence

# Reference 3: https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# Accessed 18/02/2023. Used in line 34 of script to print list without brackets or commas

# Reference 4:  https://stackoverflow.com/questions/25733737/how-to-print-out-a-string-and-list-in-one-line-python
# accessed 18/02/2023 - used for print statement in line 34 of script

# declare variable for while loop
valid_input = False

# while loop to script executes when only a positive integer is read in
while not valid_input:
    num = int(input("Please enter a positive integer: "))  # read in text
    if num == 1:  # could not find a sample code for the Collatz sequence to allow for 1 to be read in by the user
        # if statement used to solve this issue
        print(f"The Collatz sequence for {num} is 4 2 1 ")  # print this if 1 is read in by user
        break  # end script operation here if 1 is read in by user
    else:  # otherwise
        if num > 0:  # if the variable num that is read in is greater than 0 execute the following lines of code
            sequence = [num]  # declare variable called sequence to create a list populated by the num variable
            while num != 1:  # while loop when the num variable does not equal 1
                if (num % 2) == 0:  # if statement with calculation to see if the num variable is even
                    num = num // 2  # calculation to declare the value of the num variable if num is even
                else:  # otherwise execute the following lines of code
                    num = (num * 3) + 1  # calculation to declare the value of the num variable if num is odd
                sequence.append(num)  # add the num variable to the list called sequence
            print(f"The collatz sequence for {sequence[0]} is", *sequence[1:], sep=" ")  # once loop is closed and the
            # value of the num variable reaches 1 print the following statement
            valid_input = True  # close while loop
        else:
            print(f"{num} is not a positive integer.")  # statement to print if 0 or negative integer is entered. Loops
            # the user back to the original read in statement
