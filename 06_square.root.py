# This script takes a positive floating-point number as an input and outputs 
# an approximation of its square root.

# References: 
# https://en.wikipedia.org/wiki/Newton%27s_method#Examples 
# https://www.youtube.com/watch?v=xdlIFw5EM4w



# This asks the user to input a number which they want to estimate the square root of.
num = float(input('Choose a positive floating-point number: '))


# This accounts for a situation where the user enters either zero (the square root of which is zero) or a negative number
# (which has no real square root). This script can not generate a square root for either of these scenarios.
while num <= 0:
    print ("That is not a positive number. Please try again: ")
    num = float(input('Choose a positive floating-point number: '))


# Let the initial guess be half of that number.
approx = 0.5*num


# This formula (explained in the opening comments) improves upon the initial guess, and then improves upon each subsequent improvement.
better = 0.5*(approx + (num/approx))


# This continues to iterate the formula above until the improvements upon the initial guess generate the square root.
while (better!=approx):
    approx = better
    better = 0.5*(approx +(num/approx))


# Prints out the approximate square root of the number input by the user.
print(f"The square root of {(num)} is approximately {better}")