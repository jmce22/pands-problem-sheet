# This program should: 
# prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: James McEneaney

amount1 = input('Enter amount 1 in cents: ')
amount2 = input('Enter amount 2 in cents: ')
total_cents = int(amount1) + int(amount2)
total_euro = (total_cents/100)

