import csv
from pprint import pprint


class CsvReader:
    data = []

    def __init__(self, filepath):
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=",")
            for row in csv_data:
                self.data.append(row)
        pprint(self.data)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(type(class_name, row))
        return objects

