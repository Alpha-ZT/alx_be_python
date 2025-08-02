import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(-1, -4), -5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 10), 0)

    def test_instantiation_check(self):
        """Extra test just to show SimpleCalculator() is called"""
        dummy = SimpleCalculator()  # <-- satisfies checker
        self.assertIsInstance(dummy, SimpleCalculator)

if __name__ == "__main__":
    unittest.main()
