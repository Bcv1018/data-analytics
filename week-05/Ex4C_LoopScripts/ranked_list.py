# Ranking list using  enumerate()

#List of my favorite foods
Food = ["Burrito", "Pho","tacos","Fried Rice","Sushi"]

# For loop to show the ranking of my favorite foods based on their index
for index, Food in enumerate(Food, start=1):
    if index ==1 :
      print(f"{index}.{Food} <--- Top pick!")
    else:
      print(f"{index}.{Food}")

# print just to add a line break in output window
print(f"\n")

#List of my favorite foods
Food = ["Burrito", "Pho","tacos","Fried Rice","Sushi"]

# For loop to show the ranking of my favorite foods but in reverse order!
for index, Food in enumerate(reversed(Food), start=1):
   print(f"{index}.{Food}")