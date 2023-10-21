from datetime import date
import operator

from settings import tax_percent


# Each income in format: {"year": 2023, "month": 9, "amount": 200}
incomes = [
    {"year": 2023, "month": 1, "amount": 1100},
    {"year": 2023, "month": 2, "amount": 1200},
    {"year": 2023, "month": 3, "amount": 1050},
    {"year": 2023, "month": 4, "amount": 1000},
    {"year": 2023, "month": 5, "amount": 1150},
]


def add_income():
    year = int(input("Year: "))
    today = date.today()
    if year > today.year:
        raise ValueError("Year should not be in the future")

    month = int(input("Month (1-12): "))
    if 1 > month > 12:
        raise ValueError("Month should be between 1 and 12")

    amount = float(input("Income amount: "))
    if amount < 0:
        raise ValueError("Income should not be negative")

    incomes.append({
        "year": year,
        "month": month,
        "amount": amount
    })


def print_tax():
    total_income = get_total_income()
    tax_amount = total_income * tax_percent
    print(f"Tax to be paid: {tax_amount:0.2f}")


def print_incomes():
    # if not incomes:
    # the same as
    if len(incomes) == 0:
        print("No incomes. Please start adding a new one.")
        return

    for income in incomes:
        print(f"{income['year']}/{income['month']:0>2}: {income['amount']:.2f}")

def print_stats():
    min_income = 0 if not incomes else incomes[0]['amount']
    max_income = 0 if not incomes else incomes[0]['amount']
    avg_income = 0

    for income in incomes:
        amount = income['amount']

        if amount < min_income:
            min_income = amount

        if amount > max_income:
            max_income = amount

    total_income = get_total_income()    

    if incomes:
        avg_income = total_income / len(incomes)
    
    print(f"Minimum income: {min_income:.2f}")
    print(f"Maximum income: {max_income:.2f}")
    print(f"Average income: {avg_income:.2f}")
    print(f"Total income: {total_income:.2f}")


def show_chart():
    if not incomes:
        print("No incomes. Please start adding a new one.")
        return

    for income in incomes:
        amount = income['amount']
        
        print(f"{income['year']}/{income['month']:0>2}: {'#' * int(amount // 50)}")


def get_total_income():
    return sum(map(operator.itemgetter('amount'), incomes))
    
    # the same as 
    total = 0
    
    for income in incomes:
        total += income['amount']
    
    return total
