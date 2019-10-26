import unittest
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('UnitTestAddition.csv')

    persons = self.csv_reader.get_objects_of_class('person')
    pprint(persons)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csv_reader, CsvReader)


if __name__ == '__main__':
    unittest.main()
