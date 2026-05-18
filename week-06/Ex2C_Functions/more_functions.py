# Displaying mailing label formatted in mailling format
def display_mailing_label(name,address,city,state,zip):
    return f'{name}\n{address}\n{city},{state} {zip}'


#Adding numbers with each argument being an integer
def add_numbers(*args):
    result = sum(args)
    equation = " + ".join([str(n) for n in args])
    return f"{equation} = {result}"


# Displaying receipt
def display_receipt(total_due,amount_paid):
    print(f"Amount Paid: ${amount_paid}")
    print(f"Total Due: ${total_due}")
    

    if amount_paid < total_due:
        balance = total_due - amount_paid
        return f"The remaining balance to be paid is ${balance}"
    else: 
        change = amount_paid - total_due
        return f"Change Due: ${change}"


# Test
#Display mailing label
print(display_mailing_label('Brandon Carrillo-Valencia','123 Main St', 'San Jose','CA','12345'))
print('\n')
print(display_mailing_label('john doe','123 mcgrady','Austin','Texas','12345'))
print('\n')
# Add numbers
print(add_numbers(1))
print(add_numbers(1,2))
print(add_numbers(5,3,7))
print('\n')
# Displaying receipt
print(display_receipt(30,40))
print(display_receipt(40,40))
print(display_receipt(50,40))
