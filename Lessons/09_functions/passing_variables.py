def get_total(amount, qty, discount=0):
    return amount*qty - (amount*qty) * discount

# from user input
# amount = float(input("Enter amount: "))
# or as a particular value
amount = 100
total = get_total(amount, 2)
print(f"Total: {total:.2f}")

def increase_values(values):
    new_values = values

    idx = 0
    while idx < len(new_values):
        new_values[idx] = new_values[idx] * 2
        idx += 1

numbers = [1, 2, 3, 4, 5]
print(f"Numbers before function call: {numbers}")
increase_values(numbers)
print(f"Numbers after function call: {numbers}")

# but not
# increase_values((1, 2, 3, 4, 5))
