import csv
from pprint import pprint


class CsvReader:

    def __init__(self, filepath):
        self.csv_data = None
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=",")
            for row in csv_data:
                self.data.append(row)
        pprint(self.data)
