# Working with classes

# Class for resturant and description of food and if open or not
class restaurants:
    '''Restaurant description'''
    def __init__(self,name,food):
        self.name = name
        self.food = food

    def describe_rest(self):
        return f'{self.name} serves {self.food}'
    
    def rest_open(self):
        return f'{self.name} is open'
    

# 3 examples\
restaurant1 = restaurants('in-n-out', 'burgers')
restaurant2 = restaurants('popeyes','chicken')
restaurant3 = restaurants('dominoes','pizza')

# Call each method
print(restaurant1.describe_rest())
print(restaurant1.rest_open())

print('\n')

print(restaurant2.describe_rest())
print(restaurant2.rest_open())

print('\n')

print(restaurant3.describe_rest())
print(restaurant3.rest_open())