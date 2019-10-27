import unittest
from NLcalculator import NLCalculator
from csvreader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = NLCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, NLCalculator)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.division(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

        self.assertEqual(self.calculator.division(2, 1), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(3, 1), 3)
        self.assertEqual(self.calculator.result, 3)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(4), 16)
        self.assertEqual(self.calculator.result, 16)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(25), 5)
        self.assertEqual(self.calculator.result, 5)

    def print(self):
        pprint()

if __name__ == '__main__':
    unittest.main()
