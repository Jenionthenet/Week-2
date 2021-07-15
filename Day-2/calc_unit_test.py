from calc import Calculator
import unittest

class CalculateTests(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(5, result)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(5, 4)
        self.assertEqual(1, result)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(6, 2)
        self.assertEqual(12, result)

    def test_divide(self):
        calculator = Calculator()
unittest.main()
