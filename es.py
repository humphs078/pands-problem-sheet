# es.py
# Author: Sean Humphreys
# Script to count the number of times the letter "e" appears in a text file. The text file is read in as an argument
# from the command line e.g. python es.py some_file_name.txt

# Reference 1 - https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
# last accessed 09/03/2023

# Reference 2 - https://www.tutorialspoint.com/python/python_command_line_arguments.htm# last accessed 09/03/2023

# Reference 3 - https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# last accessed 09/03/2023

# Reference 4 - https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python last accessed 16/04/2023

# Reference 5 - https://realpython.com/command-line-interfaces-python-argparse/ last accessed 16/04/2023

# Assumptions:
# The user only ever wants to count the letter "e" in the given text file. This can be changed by changing the argument
# in line 39 & 44 of the code
# The total number of times the letter "e" appears in both upper and lower case should be counted
# The .txt file will be stored in the same directory as the es.py script

# import the argparse module, required to pass the filename as a command line argument. The argparse library was used
# because of the help option to direct the user if the -h switch is used. If the user does not enter a filename as an
# argument  they are passed instructions on the script usage via the command line interface
import argparse

parser = argparse.ArgumentParser()  # Create an argument parser by instantiating ArgumentParser.
parser.add_argument('filename')  # Add argument "filename" to the parser using the .add_argument() method.
args = parser.parse_args()  # Call .parse_args() on the parser to get the Namespace of arguments.


def no_of_letters(letter):
    with open(args.filename) as file:  # open the file passed as an argument as a variable called "file"
        contents = file.read()     # declare a variable called "contents" that reads in the contents of the file
    return contents.count(letter)   # return the count of the letter passed in the argument of the function


# Declare variable to count the letter passed in the argument, in this case "e". Can be changed if required
count = no_of_letters("e")
# print statement for formatted string using the "count" variable
print(f"The character \"e\" appears {count} times in the file {args.filename}.\n")

# Count the number of capital "E" occurrences
count_2 = no_of_letters("E")

# Define variable to total the number of es
total_count = count + count_2

# print statement for formatted string using the "count_2" variable
print(f"The character \"E\" appears {count_2} times in the file {args.filename}.\n")

# print statement that lets the user know the total amount of es in the txt file read in
print(f"The letter \"e\" appears a total number of\033[1;32m \033[1m{total_count}\033[0m times in the file "
      f"{args.filename}.\n")
