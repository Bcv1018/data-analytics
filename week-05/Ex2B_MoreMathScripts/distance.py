# This script is for calculating distances between two  different coordinates
# Distance formula using square roots: square root over (x2 - x1)^2 + (y2 - y1)^2 


import math 

# Points for the different coordinates which the format is (x1,y1) (x2,y2)
x1 = int(input("Type in your x1 value "))
y1 = int(input("Type in your y1 value "))
x2 = int(input("Type in your x2 value "))
y2 = int(input("Type in your y2 value "))


distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# #Display the results
print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance:.0f}")

