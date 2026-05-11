# Ranking list using  enumerate
Food = ["Burrito", "Pho","tacos","Fried Rice","Sushi"]

for index, Food in enumerate(Food, start=1):
    if index ==1 :
      print(f"{index}.{Food} <--- Top pick!")
    else:
      print(f"{index}.{Food}")

print(f"\n")

Food = ["Burrito", "Pho","tacos","Fried Rice","Sushi"]

for index, Food in enumerate(reversed(Food), start=5):
   print(f"{index}.{Food}")