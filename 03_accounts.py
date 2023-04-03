# This script takes an input of ten digits and outputs the first six digits, followed by the letter 'X' in place of the 
# last four digits
# Author: James McEneaney

# the user is asked to enter a ten digit number. the output is in 
x = input("please enter a ten digit number: ")

# the variable below is a string containing the last four digits of the ten digit number input by the user (in string format) 
# and adds a string of six 'X' characters to this four digit number
modifiedx = f'{"XXXXXX"}{x[-5:-1]}'

# this prints out ten the above ten-digit account number with first six digits hidden
print(modifiedx)