# Department name lookup based on dept code

# Department names with their code
# 1 Marketing
# 5 Human Resources
# 10 Accounting
# 12 Legal 
# 18 IT
# 20 Customer Relations

# Input statement to get the use to type in the code 
Code_num = int(input("Please type in department number: "))

if Code_num == 1:
    print("Marketing Department")
elif Code_num == 5:
    print("Human Resources Department")
elif Code_num == 10:
    print("Accounting Department")
elif Code_num == 12:
    print("Legal Department")
elif Code_num == 18:
    print("IT Department")
elif Code_num == 20:
    print("Customer Relations Department")
else:
    print("Department number is not valid")
