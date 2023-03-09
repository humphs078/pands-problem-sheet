# task_7_es.py
# Author: Sean Humphreys
# Script to read count the number of times the letter "e" appears in a text file
# Reference 1 - https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
# last accessed 03/09/2023


# Assumptions


import sys

file = sys.argv[1]


def no_of_letters(letter):
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    return contents.count(letter)


count = no_of_letters("e")
print(f"The letter \"e\" appears {count} times in the file {file}")
