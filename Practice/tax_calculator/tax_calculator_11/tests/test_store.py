import unittest
import tempfile
import json

from app.models import Income
from app.store import Storage


class TestFileStorage(unittest.TestCase):
    def test_load(self):
        """should load data from the file"""

        _, filename = tempfile.mkstemp(text=True)
        with open(filename, "w") as f:
            json.dump([{
                "year": 2023,
                "month": 1,
                "amount": 1000.0
            }], f)

        store = Storage(filename)
        store.load()

        self.assertEqual(len(store.incomes), 1)
    
    def test_save(self):
        """should save data to the file"""

        _, filename = tempfile.mkstemp(text=True)

        store = Storage(filename)
        store.add_income(Income(2022, 1, 1000))
        store.save()

        with open(filename) as f:
            data = json.load(f)

            self.assertEqual(len(data), 1)

            element = data[0]
            self.assertDictEqual(element, {
                "year": 2022,
                "month": 1,
                "amount": 1000.0
            })


if __name__ == "__main__":
    unittest.main()
