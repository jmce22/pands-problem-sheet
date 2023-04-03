# This script takes in inputted integer of any size and replaces all digits
# with the letter 'X', apart from the last four digits.
# I assume that any number inputted will be at least seven digits long, as there is limited
# usefulness in hiding only one digit from a five digit account number, or two digits from a six digit account number.
# An account number of four digits or fewer cannot benefit from a code which hides all but the last four digits.
# Author: James McEneaney

# This asks the user to input a valid number for the purpose of this exercise
x = input("please enter a number containing seven or more digits: ")

# This variable establishes how many 'X' characters will be placed before the last four digits of the account number.
# it subtracts four from the number of digits contained within the number inputted by the user and stores this as 
# an integer for use in the next line of the script
intx = int(len(x)-4)

# This variable represents the string of 'X' characters which will precede the last four digits of the account number 
numberofx = intx*"X"

# This prints a string of 'X' characters up to replace each digit up to but not including the fourth last digit, 
# and then prints out the last four digits
print(f"{numberofx}{x[-5:-1]}")