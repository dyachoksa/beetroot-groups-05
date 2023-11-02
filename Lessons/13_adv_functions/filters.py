"""
The filters.py shows example of using functions as agruments 
for another functions and how we can use them in a sequential processing.
"""

import random

def init(length, generator):
    result = []

    for _ in range(length):
        result.append(generator())

    return result

def create_amount():
    return random.randint(10_000, 15_000)

amounts = init(5, create_amount)
print(amounts)

# we need to apply 10% discount (if needed)
# then 5% shippings (if needed)
# then 11% taxes (if needed)
# for this example it will be random

def discount(value):
    need_to_apply = random.choice((True, False))

    if not need_to_apply:
        return value
    
    return value - value * 0.1


def shipping(value):
    need_to_apply = random.choice((True, False))

    if not need_to_apply:
        return value
    
    return value + value * 0.05


def tax(value):
    need_to_apply = random.choice((True, False))

    if not need_to_apply:
        return value
    
    return value + value * 0.11


def apply_filters(values, *filters):
    """Applies a list of filters to each items in the values agrument"""

    if not filters:
        return values

    totals = []
    for value in values:
        total = value

        for filter in filters:
            total = filter(total)

        # discount
        # total = discount(total)

        # shipping
        # total = shipping(total)

        # tax
        # total = tax(total)

        totals.append(total)
    
    return totals

totals = apply_filters(amounts, discount, shipping, tax)
print(f"Totals with discount, shipping and tax: {totals}")

totals = apply_filters(amounts, discount, shipping)
print(f"Totals with discount and shipping: {totals}")

# def add_1M(value):
#     return value + 1_000_000

add_1M = lambda x: x + 1_000_000

totals = apply_filters(amounts, add_1M)
print(f"Totals with 1_000_000 added: {totals}")
