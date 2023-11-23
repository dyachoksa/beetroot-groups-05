import unittest

from app.calculator import TaxCalculator
from app.models import Income
from app.store import MemoryStorage


incomes = [
    Income(2022, 8, 1000),
]


class TestCalculator(unittest.TestCase):
    def test_load_incomes(self):
        storage = MemoryStorage(incomes=incomes.copy())
        calculator = TaxCalculator(storage=storage)

        result = calculator.get_incomes()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].amount, 1000)
    
    def test_add_income(self):
        year, month, amount = 2023, 1, 2000

        storage = MemoryStorage(incomes=incomes.copy())
        calculator = TaxCalculator(storage=storage)

        calculator.add_income(year, month, amount)

        result = calculator.get_incomes()

        self.assertEqual(len(result), 2)

    def test_tax_calculation(self):
        storage = MemoryStorage(incomes=[Income(2022, 8, 1000)])
        calculator = TaxCalculator(storage=storage)

        result = calculator.get_tax()

        self.assertEqual(result, 140)

    def test_stats_calculation(self):
        storage = MemoryStorage(incomes=[
            Income(2022, 8, 1000), Income(2022, 9, 2000),
        ])
        calculator = TaxCalculator(storage=storage)

        stats = calculator.get_stats()

        self.assertDictEqual(stats, {
            "min": 1000.0,
            "max": 2000.0,
            "avg": 1500.0,
            "total": 3000.0,
        })


if __name__ == "__main__":
    unittest.main()
