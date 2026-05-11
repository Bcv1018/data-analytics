# displaying a greeting based on the current hour

current_hour = int(input("Please type in the current hour (0-23) "))


if current_hour < 10:
        print("Good Morning!")
elif current_hour < 17:
        print("Good Day!")
else:
        print("Good Evening!")



if current_hour >= 23 or current_hour < 4:
    print("What are you doing up so late??")