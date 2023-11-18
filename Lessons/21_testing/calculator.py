from functools import reduce


def add_numbers(*numbers):
    if not len(numbers):
        raise TypeError("At least one number should be provided")
    
    # for number in numbers:
    #     if not isinstance(number, int | float):
    #         raise ValueError("Only int and/or float are allowed")
    ## or
    if not all(map(lambda n: isinstance(n, int | float), numbers)):
        raise ValueError("Only int and/or float are allowed")

    return sum(numbers)


def mul_numbers(*numbers):
    if not len(numbers):
        raise TypeError("At least one number should be provided")

    for number in numbers:
        if not isinstance(number, int | float):
            raise ValueError("Only int and/or float are allowed")

    return reduce(lambda x, y: x * y, numbers)


def add_mul(*numbers):
    return add_numbers(*numbers) + mul_numbers(*numbers)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = add_numbers(0, *numbers)
    print(f"sum({numbers}) = {result}")

    numbers = [1, 2, 3, 4]
    result = mul_numbers(1, *numbers)
    print(f"mul({numbers}) = {result}")
