# type hint is not a validation
def get_total(amount: int | float, qty, discount=0.0):
    # to validate types we need to have manual checks
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("amount should be int or float and > 0")
    
    if not isinstance(qty, int) or qty <= 0:
        raise ValueError("qty should be int and > 0")

    if not isinstance(discount, (int, float)) or (discount < 0 or discount > 1):
        raise ValueError("discount should be int or float")

    return (amount*qty) - (amount*qty)*discount

total = get_total(100, 2, 0.1)
print(f"Total: {total:.2f}")

# will produce an error in runtime
# get_total("100", 2)


# Function with variable length of arguments
def sum_numbers(*numbers):
    print(f"Func arguments: {numbers}")

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("all arguments should be int or float")

    total = 0
    for number in numbers:
        total += number

    return total

sum_numbers(1)
sum_numbers(1, 2)
sum_numbers(1, 2, 3)
# will produce an error in runtime
# sum_numbers(1, 2, "3", 4)


# Function with variable keyword arguments
def make_user(**fields):
    print(f"Func arguments: {fields}")

make_user(name="Sergey")
make_user(name="Sergey", age=18)
make_user(name="Sergey", age=18, email="sergey@example.com")


# Complex definition
def complex_function(amount, qty, *args, **kwargs):
    print(f"{amount=}, {qty=}, {args=}, {kwargs=}")

complex_function(100, 2)
complex_function(100, 2, 0.1)
complex_function(100, 2, 0.1, age=18, name="Sergey")
