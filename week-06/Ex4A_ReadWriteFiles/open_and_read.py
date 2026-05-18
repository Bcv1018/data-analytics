# Using read
# no limit to read
about = open("about_me.txt",'r')
# print(about.read())

# read(50) twice
# print(about.read(50))
# print(about.read(50)) # if you add the second read 50 it will just add 50 more charaters to the first print just essentailly making it as if you did read(100)

about.close()



# using readline
about = open("about_me.txt",'r')
# # print(about.readline(10)) # if its just this it only prints 1 line which is a)
# # print(about.readline()) # if its just htis it only prints 1 line which is a)
# # for i in range(1,5): # if its just this it prints from a) to b) line with spaces in them 
# #     print(about.readline()) # if its all it prints from a) name to the answer of b) place of birth with spaces after each line
about.close()

# using readlines
about = open("about_me.txt",'r')
# print(about.readlines(1))# I get a list with the first line
# print(about.readlines(1)) # second list appears with line 2
# print(about.readlines(10)) # third list appears with the line 12?
# print(about.readlines(10)) # makes two list but the first list combines line 1 and 2 and the second combines line 4 and line 5?
# print(about.readlines(100)) # adds a third list that has the rest of the lines till question c
# print(about.readlines(-1)) # adds everything into a list

about.close()

# 3 different variables
about = open("about_me.txt", 'r')

#first variable
first_v = about.read(50)

# second variable
second_v = []
for i in range(1,5):
    second_v.append(about.readline())

# third variable
third_v = about.readlines(100)


# 3 variable outputs
print(f'First 50 characters: {first_v}')
print(f'Next four lines, as list by line: {second_v}')
print(f'Next 100 charcters, as list by line, rounded up to complete lines: {third_v}')

about.close()