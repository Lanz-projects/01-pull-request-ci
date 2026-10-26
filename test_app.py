import unittest

from app import add, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtracts_two_numbers(self):
        self.assertEqual(subtract(8, 3), 5)
    
    def test_multiplys_two_numbers(self):
        self.assertEqual(multiply(4,5), 20)

    def test_divides_two_numbers(self):
        self.assertEqual(divide(10, 2), 3)
if __name__ == "__main__":
    unittest.main()
