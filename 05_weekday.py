# This program tells the user whether today is a weekday or weekend.
# Author: James McEneaney
# References: 
# https://www.w3schools.com/python/python_datetime.asp
# https://pynative.com/python-get-the-day-of-week/#:~:text=Use%20the%20weekday()%20method,its%20weekday%20number%20is%200.

# This access the datetime module which allows us to access and manipulate data about dates and time 
import datetime

# this creates an object which represents the current date and time
today = datetime.datetime.now()

# get the day of the week as an integer, with 0 representing Monday, up to 6 representing Sunday
dayofweek = today.weekday()

# if dayofweek outputs the integer 5 or 6, this means it is Saturday or Sunday. The piece of code today.strftime("%A") generates the 
# name of the day

if int(dayofweek) > 4: 
    print(f'"Today it is {today.strftime("%A")}, which thankfully is the weekend!')
else:
    print(f'"Today it is {today.strftime("%A")}, which unfortunately is a weekday!')