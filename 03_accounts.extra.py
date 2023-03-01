# This code takes in inputted integer of any size and replaces all digits
# with the letter 'X', apart from the last four digits.
# I assume that any number inputted will be at least seven digits long, as there is limited
# usefulness in hiding only one digit from a five digit account number, or two digits from a six digit account number.
# An account number of four digits or fewer cannot benefit from a code which hides all but the last four digits.
# Author: James McEneaney

x = input("please enter a number containing seven or more digits: ")

intx = int(len(x)-4)

numberofx = intx*"X"

print(f"{numberofx}{x[-5:-1]}")