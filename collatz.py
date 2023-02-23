# This code deminstrates the Collatz conjecture. 
# According to Wikipedia, this conjecture asks whether repeating the two simple arithmetic operations 
# below will eventually transform every positive integer into 1.
# The two operations are:
# if the previous term is even, the next term is one half of the previous term. 
# If the previous term is odd, the next term is 3 times the previous term plus 1. 
# The conjecture is that for any positive integer chosen, these sequences always reach 1.
# Author: James McEneaney

n = int(input('Enter a number greater than 1: '))
print(n)
while n > 1:
    if (n % 2) == 0 :
        n = n//2
        print(n)
    else:
        n = 3*n + 1
        print(n)