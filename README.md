# pands-problem-sheet

## Contents
[Description](#Description)

[Scripts](#Scripts)

1. [Week 1 - Hello World](#Task-1---Hello-World)
2. [Week 2 - Bank](#Task-2---Bank )
3. [Week 3  - Accounts](#Task-3---Accounts)
4. [Week 3  - Accounts Modified](#Task-3a---Accounts-Modified)
5. [Week 4 - Collatz](#Task-4---Collatz)
6. [Week 5 - Weekday](#Task-5---Weekday)
7. [Week 6 - Square Root](#Task-6---Square-Root)
8. [Week 7 - Count of the Letter "e" in a txt File](#Task-7---Count-of-the-letter-e)
9. [Week 8 - Plotting](#task-8---plotting)
## Description
This repository contains the solutions to the weekly tasks for the Programming and Scripting module on the ATU 
Mayo Galway H Dip in Computer Programming and Data Analytics.

## Scripts
- - - -
### [Task 1 - Hello World](hello_world.py)

Week 1 Task - script to print **"Hello World!"** string in bold.

#### Reference
https://blog.finxter.com/how-to-print-bold-text-in-python/ - Last accessed 23/02/2023
- - - -

### [Task 2 - Bank](bank.py)

Week 2 task - script to enter two amounts in cents, add them and print out the total in human-readable format.
The output has a euro sign in front of the total. Euros and cents are separated by a decimal point.

**Reflection** - The original solution implemented used floating point integers, however this can lead to issues when 
performing arithmetic as base 10 decimals numbers are being converted to base 2 decimal numbers. The problem is that 
most decimal numbers cannot be expressed exactly in binary. This is overcome by converting the class of the integer 
read in by the user to the decimal.Decimal class from the decimal library.

#### References
+ https://learnpython.com/blog/count-money-python/ - last accessed 12/04/2023
+ https://docs.python.org/3/library/decimal.html - last accessed 12/04/2023
- - - -

### [Task 3 - Accounts](accounts.py)

Week 3 Task - Script to read in a bank account number display only the last 4 digits and mask the rest.

Assumptions:

+ the account number has to be 10 numbers. It cannot be greater or less than 10 numbers in length.
+ the account number can only contain numbers. It cannot contain letters.
+ loop statements and the use of if and else statements are permitted in the script.

**Reflection** - the challenge was to create the code so that the user could only enter a 10-digit number. The solution 
@ https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input -
last accessed 11/02/2023, was to implement a "while loop" so that if the user enters anything but a 10-digit number the
code loops back and instructs the user that what they have entered is not valid and to re-enter a valid input.

- - - -

### [Task 3a - Accounts Modified](accounts_modified.py)

Week 3 task - Script to read in bank account number of any length and display the last 4 digits of the account number 
for account numbers greater than 4 digits in length.

#### Reference
https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input - Last accessed 
11/02/2023
- - - -

### [Task 4 - Collatz](collatz.py)

Week 4 task - Script to read out the Collatz sequence for any positive integer the user reads in.

Named after mathematician Lothar Collatz (https://en.wikipedia.org/wiki/Lothar_Collatz), the Collatz conjecture 
(https://en.wikipedia.org/wiki/Collatz_conjecture) asks whether repeating two simple arithmetic operations will 
eventually transform every positive integer into 1.

**Reflection** - The challenge was if a user read in a value of 1. No function or script could be found to mitigate 
against this so a crude solution was implemented in lines 25 - 28 of the script. If the integer 1 is read in there is 
only 1 possible outcome, thus the overhead of three additional lines of code was considered justified for the sake of 
completeness.

#### References
+ https://stackoverflow.com/questions/25457923/how-to-make-python-goto-a-previous-line-to-get-more-input -
Last accessed 11/02/2023
+ https://hackernoon.com/implementing-3x1-in-python - Last accessed 18/02/2023
+ https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row - Last accessed 18/02/2023
+ https://stackoverflow.com/questions/25733737/how-to-print-out-a-string-and-list-in-one-line-python - Last accessed 
18/02/2023
- - - -

### [Task 5 - Weekday](weekday.py)

Week 5 task - Script to read out a message indicating if today is a weekday or the weekend.

This script was tested on both a **weekday and weekend** to ensure that the output was correct.

**Reflection** - the challenge was that the days of the week are outputted as integer values. An "if" statement was used 
to translate the day of the week to out a string indicating if it is a weekday or the weekend 

#### Reference
https://pynative.com/python-get-the-day-of-week/ - Last accessed 22/02/2023
- - - -
### [Task 6 - Square Root](square_root.py)
Week 6 task - Script to return the square root of a number using Newton's method.

In numerical analysis, Newton's method, also known as the Newton–Raphson method 
(https://en.wikipedia.org/wiki/Newton%27s_method), named after Isaac Newton(https://en.wikipedia.org/wiki/Isaac_Newton) 
and Joseph Raphson (https://en.wikipedia.org/wiki/Joseph_Raphson), is a root-finding algorithm which produces 
successively better approximations to the roots (or zeroes) of a real-valued function.

**Reflection** - the precision of the output was the challenge. Precision was achieved by the use of a "for" loop
iterating 100 times within a function.

#### References
+ https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula.aspx -
Last accessed 02/03/2023
+ https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo - 
Last accessed 02/03/2023
- - - -
### [Task 7 - Count of the letter **e**](es.py)
Week 7 task - Script to count the number of times the letter "e" appears in a text file. The text file is read in as an 
argument from the command line as an argument e.g. es.py some_file.txt


Assumptions:

+ The user only ever wants to count the letter "e" in the given text file. This can be changed by changing the argument
in line 45 & 49 of the code 
+ The total number of times the letter "e" appears in both upper and lower case should be counted 
+ The .txt file will be stored in the same directory as the es.py script

**Reflection** - The challenge was running the script from the command line with the desired text file being read in 
as a command line argument. This was solved by using sys library and using the sys.argv[1] in a global variable. The 
use of global variables in functions is not encouraged however is justified in this use case. Try and except blocks were
used for exception handling. Should the user omit the filename as an argument from the command line, the error is caught 
and the user is directed to enter a filename. If the user attempts to execute the script and pass a filename that is not 
valid or not located in the same directory as the script, the error is caught and the user is presented with guidance on 
how to execute the script properly.

#### References
+ Reference 1 - https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python 
last accessed 09/03/2023 
+ Reference 2 - https://www.geeksforgeeks.org/python-sys-module/ last accessed 09/03/2023 
+ Reference 3 - https://www.tutorialspoint.com/python/python_command_line_arguments.htm# last accessed 09/03/2023
+ Reference 4 - https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
last accessed 09/03/2023 
+ Reference 5 - https://www.w3schools.com/python/python_try_except.asp last accessed 18/04/2023 
+ Reference 6 - http://hplgit.github.io/primer.html/doc/pub/input/._input-solarized007.html last accessed 18/04/2023

---
### [Task 8 - Plotting](plottask.py)

Week 8 task - Script called plottask.py that displays a histogram of a normal distribution of 1000 values with a mean
of 5 and standard deviation of 2 and a plot of the function h(x)=n^3 in the range [0, 10] on the one set of axes.

**Reflection** - The challenge was formatting the outputted plot chart in a presentable way that is easily read. The 
solution was to implement a number of font and plot formatting options in the code. Below is the plot that is outputted
from the script. As can be seen it displays:

+ a histogram for the range of values generated showing the frequency of distributions of these values
+ a plot of the function h(x)=n^3

![plottask.py Plot](Figure_1.png "plottask.py Plot")

#### References
+ https://www.w3schools.com/python/numpy/numpy_random_normal.asp - last accessed 16/03/2023
+ https://www.w3schools.com/python/matplotlib_intro.asp - last accessed 16/03/2023
+ www.w3schools.com/python/matplotlib_labels.asp - last accessed 16/03/2023
+ https://www.w3schools.com/colors/colors_names.asp - last accessed 16/03/2023
+ https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/ - last accessed 23/03/2023

---