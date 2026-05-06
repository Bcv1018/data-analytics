# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print('The Total due is ' + str(total_due)) 
# str () function is being used to convert the float data type into a str data type so python can add both 'strings' togerther and display the results

print('Food cost is ' + str(food_cost) + ' and tax is ' + str(tax))
#print('Tip is ' + str(tip))
print('Tip is ' + format(tip, '.2f'))
print('Total due is ' + str(total_due))
