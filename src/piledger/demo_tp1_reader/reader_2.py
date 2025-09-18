
# Alexandrine
import csv


class FileIterator:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, newline='', encoding='utf-8')
        self.reader = csv.DictReader(self.file)
    
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.reader)

    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

with FileIterator("path/to/accounts.csv") as reader:
    for account in reader:
        pass

class File:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        return FileIterator(self.path)

    def __str__(self):
        return self.path