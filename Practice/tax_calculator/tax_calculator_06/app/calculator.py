from datetime import date
import operator

from app import store
from app.models import Income
from settings import tax_percent


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

    store.incomes.append(Income(year, month, amount))
    store.save_incomes()


def reload_incomes():
    store.load_incomes()


def print_tax():
    total_income = get_total_income()
    tax_amount = total_income * tax_percent
    print(f"Tax to be paid: {tax_amount:0.2f}")


def print_incomes():
    # if not incomes:
    # the same as
    if len(store.incomes) == 0:
        print("No incomes. Please start adding a new one.")
        return

    for income in store.incomes:
        print(income.present())

def print_stats():
    min_income = 0 if not store.incomes else store.incomes[0].amount
    max_income = 0 if not store.incomes else store.incomes[0].amount
    avg_income = 0

    for income in store.incomes:
        amount = income.amount

        if amount < min_income:
            min_income = amount

        if amount > max_income:
            max_income = amount

    total_income = get_total_income()    

    if store.incomes:
        avg_income = total_income / len(store.incomes)
    
    print(f"Minimum income: {min_income:.2f}")
    print(f"Maximum income: {max_income:.2f}")
    print(f"Average income: {avg_income:.2f}")
    print(f"Total income: {total_income:.2f}")


def show_chart():
    if not store.incomes:
        print("No incomes. Please start adding a new one.")
        return

    for income in store.incomes:
        amount = income.amount
        
        print(f"{income.get_date_label()}: {'#' * int(amount // 50)}")


def get_total_income():
    return sum(map(operator.attrgetter('amount'), store.incomes))
    
    # the same as 
    # total = 0
    # for income in incomes:
    #     total += income['amount']
    # return total
