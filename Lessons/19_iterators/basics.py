import random

N_COUNT=10
N_MIN=1
N_MAX=100

# create a list of N random integers
numbers = []
for _ in range(N_COUNT):
    numbers.append(random.randint(N_MIN, N_MAX))

# or using list compr-operator
numbers = [random.randint(N_MIN, N_MAX) for _ in range(N_COUNT)]


### but we can create our own iterator to generate N random numbers
class RandomGenerator:
    def __init__(self, min_number, max_number, count=10) -> None:
        self.min = min_number
        self.max = max_number
        self.count = count
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.count:
            self.current += 1
            return random.randint(self.min, self.max)
        
        raise StopIteration


numbers = list(RandomGenerator(N_MIN, N_MAX, N_COUNT))

# usage of this list
for n in numbers:
    print(f"Random int: {n}")
