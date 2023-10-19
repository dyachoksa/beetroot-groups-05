i_am_global = "Welcome! or not..."

# Simplest definition
def greet():
    print("Hello, World!")

greet()
greet()
greet()

# Function with argument(s)
def greet_me(name):
    print(f"Welcome, {name}!")

greet_me("Sergey")

# Function with return value
def get_discount():
    return "10%"

discount = get_discount()
print(f"Your discount: {discount}")

# Function with arguments and return value
def get_total(amount, discount):
    return amount - amount * discount

total = get_total(100, 0.1)
print(f"Your order total: {total:.2f}")

# Function with keyword arguments
def get_total_with_shipping(amount=0, shipping_amount=0, discount=0):
    return amount + shipping_amount - (amount + shipping_amount) * discount

total1 = get_total_with_shipping(amount=100)
total2 = get_total_with_shipping(amount=100, discount=0.1)
total3 = get_total_with_shipping(discount=0.1, amount=100, shipping_amount=10)
print(f"Total: {total1:.2f}")
print(f"Total with discount: {total2:.2f}")
print(f"Total with discount and shipping: {total3:.2f}")
