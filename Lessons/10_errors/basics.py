def get_total(amount: int | float, qty, discount=0.0):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("amount should be int or float and > 0")
    
    if not isinstance(qty, int) or qty <= 0:
        raise ValueError("qty should be int and > 0")

    if not isinstance(discount, (int, float)) or (discount < 0 or discount > 1):
        raise ValueError("discount should be int or float")

    return (amount*qty) - (amount*qty)*discount

try:
    total = get_total("100", 2, 0.1)
    print(f"Total: {total:.2f}")
except ZeroDivisionError:
    print("You can't divide by 0")
except ValueError:
    print("Something went wrong. Please check your input data.")

print("Finished")
