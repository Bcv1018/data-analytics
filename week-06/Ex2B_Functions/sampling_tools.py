# Ex2B Lab 1 using the random library

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# Test products works
# print(products)

# Adding a product of the day feature that will choose a product randomly
prod_of_day = random.choice(products)
# Displays the randomly chosen product for product of the day
print(f'The product of the day is {prod_of_day}!')

# Randomly selects 3 products to be used in the brief usability survery
usability_survey = random.sample(products,3)
# Displays the three randomly chosen products
print(f'The three items for the survey are {usability_survey}') 

# Randomly shuffles the products list in a random order
shuffled_list = random.shuffle(products)
# Displays the randomly shuffled list
print(products)

# Randomly generates a simulated daily transaction count between 50 and 300
Daily_Trans_count = random.randint(50,300)
# Displays the randomly chosen daily transaction count
print(f'The transaction count for today is {Daily_Trans_count}')