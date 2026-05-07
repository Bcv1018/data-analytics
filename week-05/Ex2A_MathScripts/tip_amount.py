# Tip amount calculation is total bill * tip percentage = tip amount

# Total restaurant bill
Bill = float(input('What was your restaurant bill? '))

# Tip percentage for 15 percent
Tip_percentage = float(input('What percent do you want to tip? Please input in decimal format: '))

# calculation for tip amount 
Tip_Amount = Bill * Tip_percentage

# Displaying the results
print(f'The tip on a ${Bill:.2f} restaurant bill is ${Tip_Amount:.2f}')


# Some of the pitfalls I saw was that with input it made the answers already strings, so you 
# need to convert that to either integers or float if needed otherwise it will default to a string and you can't use math
# Another drawback is that for tip percentage inputting that I had to add that to please write it in decimal format
# otherwise the calculation will not work as if they put a whole number it will not be the right answer, unless
# there is a way to convert that whole number into a decimal.

# Accidentally already did lab 4 when I re wrote my display using f-string. Nice :D