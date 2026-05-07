# Formula for converting fahrenheit to Celsius is C = F-32 / 1.8

# Fahrenheit
Fahrenheit = int(input("Please type in fahrenheit tempature to convert: "))

# first half of the formula for fahrenheit
temp = Fahrenheit - 32

# Converter calculation
Convert = temp / 1.8

print(f"Fahrenheit converted to Celsius is {Convert:.2f} C")