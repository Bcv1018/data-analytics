# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# print variables and type
print("Original a's type is ",a, type(a))
print("Original b's type is ",b, type(b))
print("Original c's type is ",c, type(c))
print("Original d's type is ",d, type(d))

# New variables for int conversion
#a_int = int(a) -- ValueError
b_int = int(b)
# c_int = int(c) -- ValueError
#d_int = int(d) -- ValueError

#print(a_int) -- ValueError
print(f"int conversion for b is {b_int}")
#print(c_int)
#print(d_int)
print("For b's new type is ",type(b_int))

# New variables for float conversion
a_flt = float(a)
b_flt = float(b)
#c_flt = float(c)
#d_flt = float(d)

print(f"float conversion for a is {a_flt}")
print(f"float conversion for b is {b_flt}")
print("for a's new type is ", type(a_flt))
print("for b's new type is ", type(b_flt))

# For variable A, casting into a float then integer
a_int_flt = int(float(a))
print(f"A's new type is {a_int_flt}")

# Slicing numeric 
a_slice = float(a[1:-1])
c_slice = int(c[:3])
d_slice = int(d[-2])

print(a_slice, type(a_slice))
print(c_slice, type(c_slice))
print(d_slice, type(d_slice))

# A and D using strip
print(a.strip())
print(d.strip())
