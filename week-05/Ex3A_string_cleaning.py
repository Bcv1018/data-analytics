# String cleaning

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# Using lower on all names
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Using Title on all names
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Using replace
print(salary_1.replace("$" ,""))
print(salary_2.replace("$" ,""))
# Checking type of replace
print(type(salary_1))
print(type(salary_2))
# Chaining int with replace
int_salary1 = int(salary_1.replace("$", "").replace(",",""))
int_salary2 = int(salary_2.replace("$", "").replace(",",""))

print(int_salary1)
print(int_salary2)
print(type(int_salary1))
print(type(int_salary2))