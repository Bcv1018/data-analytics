# Displays smallest and largest numbers that are inputted in 
# inputs for numbers
a = int(input("Type in a number for a: "))
b = int(input("Type in a number for b: "))
c = int(input("Type in a number for c: "))

# Finds the smallest number
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Finds the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c


print(f"Smallest number is {smallest}")
print(f"Largest number is {largest}")