import unittest
from NLcalculator import NLCalculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = NLCalculator()
        self.assertIsInstance(calculator, NLCalculator)


if __name__ == '__main__':
    unittest.main()
