# Working with If conditional

x = 100
y = 20

# A)
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")

# B)
if x * y == y:
    x = 10
else:
    print(f"Whoops, x equals {x}")

# C)
if x < y:
    print(f"x is less than y")
    x * 2
else:
    print(f'uh oh, x is not less than y')

# D)
if x > y:
    print(f'how is x greater than y??')
else:
    print(f'x is NOT greater than y')

# E)
print(f'The final value of x is {x} and the final value of y is {y}')