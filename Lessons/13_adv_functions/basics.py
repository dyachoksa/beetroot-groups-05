# instead of 
def x10_times(x: int | float):
    return (x+10) * 10

def x2_times(x: int | float):
    return (x+10) * 2


# we can create them dynamicly
def make_multiplier(value: int | float):
    def inner(x: int | float):
        return x * value

    return inner

x10 = make_multiplier(10)
x2 = make_multiplier(2)

print("Static functions:")
print(f"10 * 2 = {x2(10)}")
print(f"10 * 10 = {x10(10)}")
print(f"5 * 10 = {x10(5)}")

print("Dynamic functions:")
value = int(input("Enter your multiplier (integer only): "))
x_times = make_multiplier(value)
num = int(input("Enter value (int only): "))
print(f"{num} * {value} = {x_times(num)}")
