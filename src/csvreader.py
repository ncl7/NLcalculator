import csv
from pprint import pprint


class CsvReader:

    def __init__(self, filepath):
        self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=",")
            for row in csv_data:
                self.data.append(row)
        pprint(self.data)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.csv_data:
            objects.append(type(class_name, (object,), row))
