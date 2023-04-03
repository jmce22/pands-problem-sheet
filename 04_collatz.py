# This script demonstrates the Collatz conjecture. 
# According to Wikipedia, this conjecture asks whether repeating the two simple arithmetic operations 
# below will eventually transform every positive integer into 1.
# The two operations are:
# if the previous term is even, the next term is one half of the previous term. 
# If the previous term is odd, the next term is 3 times the previous term plus 1. 
# The conjecture is that for any positive integer chosen, these sequences always reach 1.
# Author: James McEneaney
# References: 


n = int(input("Enter an integer greater than 1: "))

def collatz(n):

# this while loop accounts for the case where the user enters an integer which is negative or zero, and prompts them to enter
# a positive integer instead
    while int(n) <= 0:        
        print("That is not a positive integer")
        n = int(input("Enter an integer greater than 1: "))

# once the user enters a positive integer of 2 or more, the code runs
    while n >= 2:

# the second argument, end = " ", causes the numbers to printed in the one line. (Ref: 'A Whirlwind Tour of Python pg 38)
        print(n, end = " ")   

# this instructs that if a number has no remainder after being divided by two (ie. is an even number),
# that the number should be divided by 2
        if n % 2 == 0:        
            n = n // 2        

 # this instructs that if a number is odd (ie. not even), it should be trebled and have one added to it
        else:
            n = n * 3 + 1    

    print(str(1) + " :", end = "\n")
    print("And so another positive integer succumbs to the gravitational pull of the Collatz conjecture")

print(collatz(n))