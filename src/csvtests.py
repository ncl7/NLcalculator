import unittest
from csvreader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('Unit Test Addition.csv')
        self.csv_reader = CsvReader('Unit Test Subtraction.csv')
        self.csv_reader = CsvReader('Unit Test Division.csv')
        self.csv_reader = CsvReader('Unit Test Multiplication.csv')
        self.csv_reader = CsvReader('Unit Test Square.csv')
        self.csv_reader = CsvReader('Unit Test Square Root.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csv_reader, CsvReader)


if __name__ == '__main__':
    unittest.main()
