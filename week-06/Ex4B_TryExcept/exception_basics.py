# ValueError try except block
try:
    n = int("Please write a number! ")
except ValueError:
    print('Invalid Input. Has to be a number! ')
else: 
    print(n)

# NameError try except block
try:
    x
except NameError:
    print('Please define variable! ')

# TypeError try except block
try:
    b = 'hi' + 5
except TypeError:
    print('Data types can not be added together')

# SyntaxError
try:
    eval(' if if if')
except SyntaxError:
    print("There is a syntax error in the code")