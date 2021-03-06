import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(3, calculator.add(2, 1))

    def test_substraction(self):
        self.assertEqual(3, calculator.substract(5, 2))

    def test_multiplication(self):
        self.assertEqual(10, calculator.multiply(2, 5))
