# Formula to find how many tiles needed per box is L*W / 12?
# Forumla to find how many boxes you will buy is (tiles * .10) + tiles
import math

# Values
Tiles_per_box = 12
Length = int(input("What is the Length of the room? "))
Width = int(input("What is the Width of the room? "))

# How many Tiles needed for the room
Tiles_needed = math.ceil(Length * Width / Tiles_per_box)

# Checking Tiles needed math
# print(Tiles_needed)

# How many Boxes do you need
# Boxes_needed = math.ceil((Tiles_needed * .10) + Tiles_needed)
Boxes_needed = math.ceil((Tiles_needed * .10) + Tiles_needed) 

# Displaying results
print(f"You will need {Boxes_needed} tile boxes for a {Length} by {Width} room!")