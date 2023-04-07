# This script takes a positive floating-point number as input and outputs 
# an approximation of its square root.

# The Newton Raphson method can produce an accurate estimate for the square root of a number as follows:
# Let 'a' be the number whose square root we are seeking, and let a = x^2 ie. x is the square root.
# This is equivilant to finding the value for x at which the function f(x) = x*x - a = 0. 
# Therefore f'(x) = 2x

# By Newtons method, the first approximation for the square root, x(1), is equal to x(0) - (f(x(0))/ f'(x(0))), 
# where x(0) is an initial guess for the square root.

# Simplifying the notation, "better guess" = x - ((x*x - a)/(2*x))
# Provided the inital guess is a good one, a few iterations of this formula should generate an accurate 
# estimate of the square root 'x'. 

# The right hand side of the formula can be rearranged to make it easier write a script:
# "better guess" = 0.5(2*x - (x - (a/x)) 
# = 0.5(x + (a/x)) 

# References: 
# https://en.wikipedia.org/wiki/Newton%27s_method#Examples 
# https://www.youtube.com/watch?v=xdlIFw5EM4w


# ask the user to input a number which they want to estimate the square root of
num = float(input('choose a positive floating-point number: '))
    
# let the initial guess be half of that number
approx = 0.5*num

# this formula (explained in the opening comments) improves upon the initial guess, and then improves upon each subsequent improvement
better = 0.5*(approx + (num/approx))

# this continues to iterate the formula above until the improvements upon the initial guess generate the square root
while (better!=approx):
    approx = better
    better = 0.5*(approx +(num/approx))

print(f"The square root of {(num)} is approximately {better}")