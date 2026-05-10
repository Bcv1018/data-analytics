# Working with tuples

Fruity_candy = ("AirHeads","Starburst","Skittles")
Fruity_flavors = ("Strawberry","Cherry","Blue Raspberry")

# Creating set for candy combinaitons by adding both tuples
candy_combination = {
    Fruity_candy[0] +" "+ Fruity_flavors[0]
    ,Fruity_candy[1] +" "+ Fruity_flavors[1]
    ,Fruity_candy[2] +" "+ Fruity_flavors[2]
}

print(f"Today's candy options include: {candy_combination}")

# What I noticed about the order of titems after running it multiple times is that the order of the items in the set is random every time and never the same order.