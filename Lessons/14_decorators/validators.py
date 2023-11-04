import functools


def allow_integers_only(func):
    @functools.wraps(func)
    def inner(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("All arguments should be integers")
        
        return func(*args)

    return inner

def allow_numbers(func):
    @functools.wraps(func)
    def inner(*args):
        for arg in args:
            if not isinstance(arg, int | float):
                raise ValueError("All arguments should be integers")
        
        return func(*args)

    return inner


# @allow_integers_only
@allow_numbers
def calculate_total(*numbers):
    return sum(numbers)


print(calculate_total(10, 12, 11, 100))
print(calculate_total(10, 10.50, 12))
