# using a while loop to keep track of savings and when you hit savings goal

# Start
bank_balance = int(input("Type in starting balance: "))
savings_goal = int(input("Type in savings goal: "))
weekly_savings = int(input("Type in weekly savings amount: "))
#treat = int(input("What is the cost of treat once reached 75%? "))

while bank_balance < savings_goal:
    bank_balance += weekly_savings
    print(f"This week my balance increased to ${bank_balance}")

    if bank_balance >= savings_goal * .75:
        bank_balance -= int(input("What is the cost of the treat? "))
        print(f"So close! After treating myself, my balance is up to ${bank_balance} ")
    elif bank_balance >= savings_goal / 2:
        print(f"Almost there! This week my balance is up to ${bank_balance}")
else:
    print(f"Goal Met! My current balance is ${bank_balance}")
