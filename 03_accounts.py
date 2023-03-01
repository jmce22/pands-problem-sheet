# This program takes an input of ten digits and outputs the first six digits, followed by the letter 'X' in place of the 
# last four digits
# Author: James McEneaney

x = input("please enter a ten digit number: ")

modifiedx = f'{"XXXXXX"}{x[-5:-1]}'

print(modifiedx)