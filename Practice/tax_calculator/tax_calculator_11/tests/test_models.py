import unittest

from app.models import Income


class TestIncomeModel(unittest.TestCase):
    def test_model_attributes(self):
        """should have correct attributes"""

        income = Income(2022, 1, 1000)

        self.assertEqual(income.year, 2022)
        self.assertEqual(income.month, 1)
        self.assertEqual(income.amount, 1000)

    def test_optional_amount(self):
        """shpuld allow amount to be optional"""

        income = Income(2021, 1)

        self.assertEqual(income.amount, 0)
    
    def test_from_dict(self):
        """should be correctly converted from dict"""

        data = { "year": 2022, "month": 1, "amount": 1000 }

        income = Income.from_dict(data)

        self.assertIsInstance(income, Income)
        self.assertEqual(income.year, data["year"])
        self.assertEqual(income.month, data["month"])
        self.assertEqual(income.amount, data["amount"])
    
    def test_from_dict_validation(self):
        """should correctly validate incomming dict"""

        empty_data = {}
        missing_key = {"year": 2022, "amount": 1000}

        with self.assertRaises(ValueError, msg="Should not allow non-dict param"):
            Income.from_dict("missing_key")

        with self.assertRaises(ValueError, msg="Should not allow empty dicts"):
            Income.from_dict(empty_data)

        with self.assertRaises(ValueError, msg="Should not allow missing keys"):
            Income.from_dict(missing_key)
    
    def test_to_dict(self):
        """should be able to convert to dictionary"""

        income = Income(2022, 1, 1000)

        data = income.to_dict()
        expected_data = { "year": 2022, "month": 1, "amount": 1000 }

        self.assertDictEqual(data, expected_data)
    
    def test_get_month(self):
        """should return month name"""

        income = Income(2022, 1, 1000)
        month = income.get_month()

        self.assertEqual(month, "January")

    def test_str_convertion(self):
        """should convert to string"""

        income = Income(2022, 1, 1000)
        value = str(income)

        self.assertEqual(value, "1000.00")


if __name__ == "__main__":
    unittest.main()
