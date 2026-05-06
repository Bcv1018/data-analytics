# fomrula for rule of 72 is 72/ interest rate = years to double

# current savings
Current_S = 10000

# Interest rate
Rate = 8

# Doubled savings amount
Future_S = Current_S * 2

# Years to double: also rule of 72 formula
Rule_72 = 72 / Rate

print('Your current savings is', Current_S)
print('At a',format(Rate),'%','interest rate, your savings account will be worth',format(Future_S,'.2f'),'in',format(Rule_72,'.1f'),'years')