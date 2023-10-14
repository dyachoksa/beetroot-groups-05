print("Hello, world!")

# Integer: 1 2 3 1010
# Floats: 2.4 0.1 -10.1000123
# Complex (math): 1+1j
# Booleans: True False
# Strings: "abc"
# Nothing: None

# Math operations: 1 + 1, 2 - 4, 5 * 6, 5 / 7

print(1)
print(100 + 1)
print("abc" * 5)

a = 1
b = 100
print(a, b, a + b)

print(True+False)

# Won't work
# print("abc" + False)

c = b * b
print(c)

b = a + c
print(b)

# 2 ** 3 == 2 * 2 * 2

str1 = "abc"
str2 = 'abc'
print(str1, str2)

# str3 = "Is you name \"Sergey\"?"
str3 = 'Is you name "Sergey"?'
print(str3)

# Naming
# Allowed symbols: a-z, 0-9, _
# Should start with a-z or _
# Correct: age, min_value, loop_1, _x
# Wrong: 0age, !_value, 0_1

age = 18
# not
# a = 18

nm = "Sergey"  # Bad
name = "Sergey"
# or better
first_name = "Sergey"
last_name = "Dyachok"
full_name = first_name + " " + last_name

désigner = "Sergey"  # not recommended

age = 18  # max age, no so good
max_age = 18  # better
# but not
a_maximum_age_of_a_person = 18  # too long


# Casing
total_income = 1_000_000  # PEP-8 or snake-casing
totalIncome = 1_000_000  # Pascal-casing or Camel-casing
