import os
import csv

class CSVPrinter:
    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise RuntimeError(f"{file_name} is not exists")
        self.file_name = file_name 

    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [ row for row in reader ]
        return lines
