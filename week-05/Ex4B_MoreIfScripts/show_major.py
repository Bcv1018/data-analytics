# Looking for name of major and location based on major code

student_name = input("What is the student's name? ")
major_code = input("What is the major code? ")



if major_code == "BIOL":
    major_name = "Biology"
    major_loc = "Science Bldg, Room 310"
elif major_code == "CSCI":
    major_name = "Computer Science"
    major_loc = "Sheppard Hall, Room 314"
elif major_code == "ENG":
    major_name = "English"
    major_loc = "Kerr Hall, Room 201"
elif major_code == "HIST":
    major_name = "History"
    major_loc = "Kerr Hall, Room 114"
elif major_code == "MKT":
    major_name = "Marketing"
    major_loc = "Westly Hall, Room 310"
else:
    major_name = "Invalid major code"
    major_loc = "N/A"


print(student_name)
print(major_name)
print(major_loc)


