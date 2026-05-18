# Working with classes

# Class for resturant and description of food and if open or not
class restaurants:
    '''Restaurant description'''
    def __init__(self,name,food,num_served=0,cx_rating=[]):
        self.name = name
        self.food = food
        self.num_served = 0
        self.cx_rating = []

    def describe_rest(self):
        return f'{self.name} serves {self.food}'
    
    def rest_open(self):
        return f'{self.name} is open'
    
    def add_num_served(self):
        served = int(input('How many customers served today? '))
        self.num_served += served
        return self.num_served

    def print_num_served(self):
        return f'{self.name} has served {self.num_served} customers'

    def customer_rating(self):
        while True:
            try:
                rating = int(input('How would you rate your experience today on a scale of 1-5(5 being excellent)? '))
                if 1 <= rating <= 5:
                    break
                else:
                    print('Please enter a number between 1 and 5! ')
            except ValueError:
                print("Please enter a valid number!")
        self.cx_rating.append(rating)
        avg_rating = sum(self.cx_rating) / len(self.cx_rating)
        return f'Your rating was {rating}. The average rating of {self.name} is {avg_rating:.1f}'
    


# 3 examples\
restaurant1 = restaurants('in-n-out', 'burgers')
restaurant2 = restaurants('popeyes','chicken')
restaurant3 = restaurants('dominoes','pizza')

# Testing for customer served
print(restaurant1.print_num_served())
print(restaurant1.add_num_served())
print(restaurant1.add_num_served())
print(restaurant1.print_num_served())
print('\n')
print(restaurant2.print_num_served())
print(restaurant2.add_num_served())
print(restaurant2.add_num_served())
print(restaurant2.print_num_served())
print('\n')
print(restaurant3.print_num_served())
print(restaurant3.add_num_served())
print(restaurant3.add_num_served())
print(restaurant3.print_num_served())
print('\n')

# testing for customer rating
print(restaurant1.customer_rating())
print(restaurant1.customer_rating())
print('\n')

print(restaurant2.customer_rating())
print(restaurant2.customer_rating())
print('\n')

print(restaurant3.customer_rating())
print(restaurant3.customer_rating())



