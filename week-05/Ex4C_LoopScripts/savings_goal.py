# using a while loop to keep track of savings and when you hit savings goal

# starting values such as current balance, what your saving goal is, and how much you will contribute weekly
bank_balance = int(input("Type in starting balance: "))
savings_goal = int(input("Type in savings goal: "))
weekly_savings = int(input("Type in weekly savings amount: "))

# While loop to keep on adding to the bank balance until savings goal is reached
while bank_balance <= savings_goal: # While bank balance is lower than savings goal, the loop will keep going
    bank_balance += weekly_savings # While bb is lower than sg then weekly savings will be added to bb until goal bank balance is equal to or greater than savings goal 
    print(f"This week my balance increased to ${bank_balance}")

    if bank_balance >= savings_goal: # Once condition is met will output the message that goal was reached
        print(f"Goal Met! My current balance is ${bank_balance}")
        break # breaks the loop is bank balance is greater than or equal to savings goal
    elif bank_balance >= savings_goal * .75:
        bank_balance -= int(input("What is the cost of the treat? ")) # once goal reaches 75% has the option to buy a treat or not
        print(f"So close! After treating myself, my balance is up to ${bank_balance} ")
    elif bank_balance >= savings_goal / 2: # once goal is at the halfway mark or greater just prints the message below
        print(f"Almost there! This week my balance is up to ${bank_balance}")

