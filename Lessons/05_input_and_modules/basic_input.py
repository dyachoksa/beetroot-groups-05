name = input("What's your name? ")

print("Hello, " + name + ". It's a good day today!")

age = input("What's your age? ")

# age will be a string, we need to convert it to integer
# but value may not be an integer so there should be a validation
# e.g age.is_digit()
age = int(age)

print("Next year you will be " + str(age + 1) + " years old.")
