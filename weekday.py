# weekday.py
# Author: Sean Humphreys
# Script that that outputs whether or not today is a weekday.

# Reference - https://pynative.com/python-get-the-day-of-week/ Accessed 22/02/2023

# from the datetime module import datetime
from datetime import datetime

# Declare a variable to get the current date and time from the datetime module
current_date_time = datetime.now()

# Integer value of days in datetime as follows:
# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday

# Declare variable for day of week as an integer
day_of_the_week = current_date_time.weekday()
# if the value of the day of the week is between 0 to 4 print weekday
if 0 <= day_of_the_week <= 4:
    print("Yes, unfortunately today is a weekday.")
# else if the value of the day of the week int is greater than 4 print weekend
else:
    print("It is the weekend, yay!")
