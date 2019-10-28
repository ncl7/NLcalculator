import unittest
from NLcalculator import NLCalculator
from csvreader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = NLCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, NLCalculator)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrt_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
