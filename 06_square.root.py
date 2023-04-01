# This progam takes a positive floating-point number as input and outputs 
# an approximation of its square root.
# Author: James McEneaney

chosen_number = input('choose a positive floating-point number: ')
a = float(chosen_number)

first_guess = input('guess the square root of your chosen number: ')
x = float(first_guess)

def sqrt(a):

# if x is the square root of a, x*x = a. Therefore x*x - a = 0. 
# absolute value is taken. as guess can be too high or too low.
    while abs(x*x - a) > 0.0001:
        x = x - ((x*x - n)/(2*x))
    return x

print("the square root is ", float(sqrt(a)))
