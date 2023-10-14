# if statements

age = 23
name = "Sergey"

# Allowed age is between 16 and 24
if age > 16 and age < 24:
    print("Welcome back,", name)
    print("Have a good day today!")
else:
    print("You are not allowed here")

# with opposite check
# if age <= 16 or age >= 24:
#     print("You are not allowed here")
#     # exit from script or return from function here
#
# print("Welcome back,", name)
# print("Have a good day today!")


# Should be avoided
if age > 16:
    if age > 18:
        if age > 20:
            if age > 22:
                if age < 24:
                    print("You've got here!")
            elif age < 1:
                print("0")
        elif age > 60:
            print("Eldery?")
    else:
        print("not good!")

# better
if 22 < age < 24:
    print("That's better!")
elif age < 1:
    print("Are you newborn?")
