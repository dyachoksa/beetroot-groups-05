from datetime import date
import operator

from app.models import Income
from app.store import Storage
from settings import tax_percent, app_name, app_version


class TaxCalculator:
    def __init__(self, storage=None) -> None:
        self.storage = Storage() if storage is None else storage
        self.storage.load()

    def __str__(self) -> str:
        return f"{app_name}/{app_version}"

    def add_income(self, year: int, month: int, amount: int | float):
        today = date.today()
        if year > today.year:
            raise ValueError("Year should not be in the future")

        if 1 > month > 12:
            raise ValueError("Month should be between 1 and 12")

        if amount < 0:
            raise ValueError("Income should not be negative")

        self.storage.add_income(Income(year, month, amount))
        self.storage.save()

    def reload_incomes(self):
        self.storage.load()

    def get_tax(self):
        total_income = self.get_total_income()
        tax_amount = total_income * tax_percent

        return tax_amount

    def get_incomes(self):
        return self.storage.get_incomes()

    def get_stats(self):
        min_income = 0 if not self.storage.incomes else self.storage.incomes[0].amount
        max_income = 0 if not self.storage.incomes else self.storage.incomes[0].amount
        avg_income = 0

        for income in self.storage.incomes:
            amount = income.amount

            if amount < min_income:
                min_income = amount

            if amount > max_income:
                max_income = amount

        total_income = self.get_total_income()    

        if self.storage.incomes:
            avg_income = total_income / len(self.storage.incomes)
        
        return {
            "min": min_income,
            "max": max_income,
            "avg": avg_income,
            "total": total_income,
        }
    
    def get_chart_data(self):
        # lsit of tuples (label, value)
        return list(map(lambda i: (i.label, i.amount), self.storage.incomes))

    def get_total_income(self):
        return sum(map(operator.attrgetter('amount'), self.storage.incomes))
