import unittest

from app import add, subtract


class CalculatorTests(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtracts_two_numbers(self):
        self.assertEqual(subtract(8, 3), 5)


if __name__ == "__main__":
    unittest.main()
