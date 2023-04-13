# This script demonstrates the Collatz conjecture.

# References: 'A Whirlwind Tour of Python 2'
# https://www.youtube.com/watch?v=5mFpVDpKX70  



# This asks the user to input a number.
n = int(input("Enter an integer greater than 1: "))


# This creates the function used to test the Collatz conjecture.
def collatz(n):


# This while loop accounts for the case where the user enters an integer which is negative or zero, and prompts them to enter
# a positive integer instead
    while int(n) <= 0:        
        print("That is not a positive integer")
        n = int(input("Enter an integer greater than 1: "))


# Once the user enters a positive integer of 2 or more, the code runs
    while n >= 2:


# The second argument, end = " ", causes the numbers to printed in the one line. (Ref: 'A Whirlwind Tour of Python 2' pg 38)
        print(n, end = " ")   


# This instructs that if a number has no remainder after being divided by two (ie. is an even number),
# that the number should be divided by 2
        if n % 2 == 0:        
            n = n // 2        


# This instructs that if a number is odd (ie. not even), it should be trebled and have one added to it
        else:
            n = n * 3 + 1    


# This prints the number '1' to end the sequence of numbers, since the earlier part of the script stops printing
# numbers once n = 2.
    print(str(1) + " :", end = "\n")
    print("And so another positive integer succumbs to the gravitational pull of the Collatz conjecture")


print(collatz(n))