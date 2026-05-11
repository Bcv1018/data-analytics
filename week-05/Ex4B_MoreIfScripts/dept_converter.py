# Department name lookup based on dept code

# Department names with their code
# 1 Marketing
# 5 Human Resources
# 10 Accounting
# 12 Legal 
# 18 IT
# 20 Customer Relations

# Input statement to get the use to type in the code 
Dept_num = int(input("Please type in department number: "))

if Dept_num == 1:
    print("Marketing Department")
elif Dept_num == 5:
    print("Human Resources Department")
elif Dept_num == 10:
    print("Accounting Department")
elif Dept_num == 12:
    print("Legal Department")
elif Dept_num == 18:
    print("IT Department")
elif Dept_num == 20:
    print("Customer Relations Department")
else:
    print("Department number is not valid")
