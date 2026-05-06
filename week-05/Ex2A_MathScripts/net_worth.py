# Formula for calculating net worth based on assets and debts is Assets - Debts = Net Worth.  A positive number inidcates you own more than you owe and negative the opposite
# Getting values from googling avg "" in california and other different googling terms related to the assets and debts

# Assets
Checking_Account = 2800
Savings_Account = 17046 
Home_Value = 500000
Car_Value = 35759

# Total Assets amount
Total_Assets_Amount = Checking_Account + Savings_Account + Home_Value + Car_Value

# Debts

Mortgage = 3100
Student_Loans = 38300
Auto_Loans = 17879
Credit_card_Debt = 9396
Medical_bills = 4000


# Total Debts amount
Total_Debt_Amount = Mortgage + Student_Loans + Credit_card_Debt + Medical_bills 

# Net worth calculation
Net_Worth = Total_Assets_Amount - Total_Debt_Amount

# Display the results
print(f'Your total assets are: , {Total_Assets_Amount:,}')  
print(f'Your total debts are: , {Total_Debt_Amount:,}')
print(f'Your net worth is: , {Net_Worth:,}')