# Working with lists
movie_list = ["Zathura","Ed", "Kung Fu Panda","Shrek","Scooby-Doo","The Sandlot","Cars"]
print(f"The list [movie_list] inlcudes {len(movie_list)} of movies I grew up watching")
print(movie_list)

# Using sorted()
print(sorted(movie_list))
print(movie_list)
# The sorted() function lists the list in alphabetical order and without it it lists the list in the order the strings were put in

# Using .sort()
movie_list.sort()
print(movie_list)
# The .sort() acts like a variable and it also sorts it by a-z order

# Using append
movie_list.append("Star wars episode 3")
# Updated description
print(f"The list [movie_list] includes {len(movie_list)} of movies I grew up watching ")
# Updated list
print(movie_list)


