# es.py
# Author: Sean Humphreys
# Script to count the number of times the letter "e" appears in a text file. The text file is read in as an argument
# from the command line

# Reference 1 - https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
# last accessed 09/03/2023

# Reference 2 - https://www.geeksforgeeks.org/python-sys-module/ last accessed 09/03/2023

# Reference 3 - https://www.tutorialspoint.com/python/python_command_line_arguments.htm# last accessed 09/03/2023

# Reference 4 - https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# last accessed 09/03/2023

# Assumptions:
# The user only ever wants to count the letter "e" in the given text file. This can be changed by changing the argument
# in line 40 of the code
# The total number of times the letter "e" appears in both upper and lower case should be counted
# The .txt file will be stored in the same directory as the es.py script

# import the system module
import sys

# Declare variable called "file" for argument being passed in from the command line.
# The first argument, sys.argv[0] is the .py filename. That is why sys.argv[1] is used
# file = sys.argv[1]


# function to read in the contents of the text file and count the number of times the letter "e" appears
try:
    file = sys.argv[1]

    def no_of_letters(letter):  # argument letters variable. Can be changed to a different value - see line 40
        with open(sys.argv[1], 'r') as f:   # open the file passed in as an argument from the command line in read only
            # mode as variable f
            contents = f.read()     # declare a variable called "contents" that reads in the contents of the file
        # in variable "f" in line 31
        return contents.count(letter)   # return the count of the letter passed in the argument of the function this
        # can be set in line 40 of code
    # Declare variable to count the letter passed in the argument, in this case "e". Can be changed if required
    count = no_of_letters("e")
    # print statement for formatted string using the "count" and "file" variables
    print(f"The character \"e\" appears {count} times in the file {file}.\n")

    count_2 = no_of_letters("E")

    total_count = count + count_2

    print(f"The character \"E\" appears {count_2} times in the file {file}.\n")
    # print statement that lets the user know the total amount of es in the txt file read in
    print(
        f"The letter \"e\" appears a total number of\033[1;32m \033[1m{total_count}\033[0m times in the file {file}.\n")
except IndexError:
    print('A file name must be supplied in the command line e.g. python es.py example_filename.txt')
except NameError:
    print('The file specified must be a .txt file and be in the same directory as the script e.g. python es.py '
          'example_filename.txt ')
except FileNotFoundError:
    print('The file specified must be a .txt file and be in the same directory as the script e.g. python es.py '
          'example_filename.txt')
