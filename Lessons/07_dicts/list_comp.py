import random

# init list with 1000 random integers
numbers = []
for _ in range(1_000):
    numbers.append(random.randint(1, 10_000))

# but better
numbers = [random.randint(1, 10_000) for _ in range(1_000)]
