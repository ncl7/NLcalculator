import unittest
from NLcalculator import NLcalculator

class MyTestCase(unittest.TestCase)

    def test_instantiate_calculator(self):
        calculator = NLcalculator()
        self.assertIsInstance(calculator, NLcalculator)


if __name__ == '__main__':
    unittest.main()