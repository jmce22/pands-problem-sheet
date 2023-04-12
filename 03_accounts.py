# This script takes an input of ten digits and outputs the first six digits, followed by the letter 'X' in place of the 
# last four digits
# Author: James McEneaney



# This asks the user to enter a ten digit number.
x = input("Please enter a ten digit number: ")


# This accounts for the situation where the user enters more or less than ten digits, and prompts them again
# to input a ten-digit number
if len((x)) != 10:
    print("That number doesn't contain ten digits. Please try again!")
    x = input("Please enter a ten digit number: ")


# The variable below creates a string containing the last four digits of the ten digit number input by the user (in string format) 
# and precedes it with a string of six 'X' characters.
modifiedx = f'{"XXXXXX"}{x[-4:]}'


# This prints out the above ten-digit account number with first six digits hidden.
print(modifiedx)