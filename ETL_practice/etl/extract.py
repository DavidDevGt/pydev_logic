import csv

class Extractor:
    def __init__(self, file_path):
        self.file_path = file_path

        def extract_data(self):
            data = []
            with open(self.file_path, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    data.append(row)
            return data