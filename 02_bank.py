# This script prompts the user to enter in two money amounts (in cent),
# adds the two amounts and prints out the answers in a human readable format,
# with a euro sign and decimal point between the euro and cent of the amount 
# Author: James McEneaney



# This asks the user to input two amounts in succession (in cents).
amount1 = input('Enter amount 1 in cents: ')
amount2 = input('Enter amount 2 in cents: ')


# This adds the two amounts in cents and converts the result to a string format, for use in the second line, 
# where the first part prints what goes before the decimal point, then adds a decimal point, then prints the
# amount after the decimal point.
total_cents = str(int(amount1) + int(amount2))
total_euro = total_cents[:-2] + '.' + total_cents[-2:]


# This prints the result, along with a euro symbol.
print("€"+ str(total_euro))