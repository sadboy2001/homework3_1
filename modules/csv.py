import csv
from files import CSV_FILE_PATH
def takeBooks():
    with open(CSV_FILE_PATH, newline='') as f:
        reader = csv.reader(f)

        header = next(reader)
        books = []

        for row in reader:
            books.append(dict(zip(header, row)))

        return books
