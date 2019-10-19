import unittest
from NLcalculator import NLCalculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = NLCalculator()
        self.assertIsInstance(calculator, NLCalculator)

    def test_results_property_calculator(self):
        calculator = NLCalculator()
        self.assertEquals(calculator.result, 4)

    def test_add_method_calculator(self):
        calculator = NLCalculator()
        self.assertEqual(calculator.add(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
