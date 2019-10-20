import unittest
from NLcalculator import NLCalculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = NLCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, NLCalculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 2)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 1), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.division(2, 1), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(3, 1), 3)
        self.assertEqual(self.calculator.result, 3)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(4), 16)
        self.assertEqual(self.calculator.result, 16)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(25, 5), 5)
        self.assertEqual(self.calculator.result, 5)


if __name__ == '__main__':
    unittest.main()
