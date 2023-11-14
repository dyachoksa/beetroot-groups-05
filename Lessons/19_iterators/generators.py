import random
import math


def random_generator(count, min_number, max_number):
    for _ in range(count):
        yield random.randint(min_number, max_number)


def random_sqrt(count):
    for _ in range(count):
        yield math.sqrt(random.randint(100, 1000))


# we convert it to list if it's needed to be used in more then one place
numbers = list(random_generator(10, 1, 100))
print(f"Min number: {min(numbers)}")
print(f"Max number: {max(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")

# other cases - just simple loop
for number in random_generator(5, 1, 100):
    print(f"Random number: {number}")
