# This script prompts the user to enter in two money amounts (in cent),
# adds the two amounts and prints out the answers in a human readable format,
# with a euro sign and decimal point between the euro and cent of the amount 
# Author: James McEneaney



# This asks the user to input two amounts in succession (in cents)
amount1 = input('Enter amount 1 in cents: ')
amount2 = input('Enter amount 2 in cents: ')

# These add the two amounts inputted, divide the amount by 100 (converting the sum to the equivilant number of euros)
# and stores this number as a floating point number.
total_cents = int(amount1) + int(amount2)
total_euro = float(total_cents/100)

# This prints the result, along with a euro symbol
print("€"+ str(total_euro))