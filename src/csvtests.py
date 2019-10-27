import unittest
from csvreader import CsvReader, ClassFactory
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('UnitTestAddition.csv')
        self.csv_reader = CsvReader('Unit Test Subtraction.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csv_reader, CsvReader)


if __name__ == '__main__':
    unittest.main()
