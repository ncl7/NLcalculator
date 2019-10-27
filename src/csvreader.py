import csv
from pprint import pprint


class CsvReader:

    def __init__(self, filepath):
        data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=",")
            for row in csv_data:
                data.append(row)
        pprint(data)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(type(class_name, (object,), row))
        return objects

