# Department lookup v2 using match case

# Department names with their code
# 1 Marketing
# 5 Human Resources
# 10 Accounting
# 12 Legal 
# 18 IT
# 20 Customer Relations


Dept_num = int(input("Please type in the Department number: "))

match Dept_num:
    case 1:
        print("Marketing Department")
    case 5:
        print("Human Resources Department")
    case 10:
        print("Accounting")
    case 12:
        print("Legal Department")
    case 18:
        print("IT Department")
    case 20:
        print("Customer Relations")
    case other:
        print("Invalid Department number")
