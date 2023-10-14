# Boolean: True False

# Maths: >, >=, <, <=, ==

1 > 2  # False
500 < 1000  # True

"abc" > "bc"  # True

3.0 == 3.0  # True, sometimes False

1 == 1  # always True

# Logical: or, and, not, is, in

age = 18
name = "Sergey"

name is None  # False
name is not None  # True

# Allowed age is between 16 and 24
# two checks
age > 16
age < 24
# or one check
age > 16 and age < 24  # True for 18, False for 14 or 26

# Order of operation

((age + 10 > 18) or age < 10) and name is not None
