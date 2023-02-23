# helloworld.py
# Author: Sean Humphreys
# Script to print 'Hello World!' string in bold
# Reference - https://blog.finxter.com/how-to-print-bold-text-in-python/ last accessed 23/02/2023

# This is a no library method to print the string in bold. "\" escape character is used to enclose the string
print("\033[1m" + "Hello World!" + "\033[0m")