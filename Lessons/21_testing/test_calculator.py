import unittest

from calculator import add_numbers, mul_numbers


class TestAddNumbers(unittest.TestCase):
    def test_several_arguments(self):
        """add_numbers() should work with correct values"""

        tests = [
            ([1, 2, 3, 4, 5], 15),
            ([10, 15], 25),
            ([100.0, 100.0, 100], 300.0),
        ]

        for numbers, expected_result in tests:
            result = add_numbers(*numbers)
            self.assertEqual(result, expected_result, 
                             f"Expected sum({numbers}) == {expected_result}")

    def test_one_argument(self):
        """add_numbers() should work with one argument"""

        result = add_numbers(10)

        self.assertEqual(result, 10)

    def test_no_arguments(self):
        """add_numbers() should accept at least one argument"""
        
        with self.assertRaises(TypeError):
            add_numbers()
    
    def test_arguments_type(self):
        """should accept only int and/or float"""

        with self.assertRaises(ValueError):
            add_numbers(1, 10, "15", 5)


class TestMulNumbers(unittest.TestCase):
    def test_several_arguments(self):
        """mul_numbers() should work with correct values"""

        numbers = [1, 2, 3, 4]
        result = mul_numbers(1, *numbers)
        expected_result = 24

        self.assertEqual(result, expected_result, f"Expected mul({numbers}) == {expected_result}")
    
    def test_one_argument(self):
        """mul_numbers() should work with one argument"""

        result = mul_numbers(10)

        self.assertEqual(result, 10)

    def test_no_arguments(self):
        """mul_numbers() should accept at least one argument"""
        
        with self.assertRaises(TypeError):
            mul_numbers()

    def test_arguments_type(self):
        """should accept only int and/or float"""

        with self.assertRaises(ValueError):
            mul_numbers(1, 10, "15", 5)


if __name__ == "__main__":
    unittest.main()
