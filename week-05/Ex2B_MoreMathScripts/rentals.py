# Formula for how many vans needed tourists/ van seats
# Forumla for how much the vans cost: Van cost * needed vans
# Formula for how much per person

import math

# Input variables to get values for certain things
Tourists = int(input("How many tourists are there? "))
Van_seats = int(input("How many seats in a van? " ))

# How many vans needed
Vans_needed = math.ceil(Tourists / Van_seats)

print(f"The amount of vans needed is {Vans_needed}")
# How much vans cost
Vans_cost = 250 * Vans_needed

print(f"The amount of cost for the vans is ${Vans_cost}")

# How much it is per person
Cost_per_person = Vans_cost / Tourists

print(f"The cost per person to rent is ${Cost_per_person:.2f}")

# A) My script said per person it will be $19.74
# B) If I multiply that out it will be 750.12
# C) For 3 vans it was $750
# D) I have leftover money because in my script it formats the money to two decimal points and is not the exact number of the cost per person