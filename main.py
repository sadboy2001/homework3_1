from modules.csv import take_books
from modules.json import gen_json

books = take_books()
gen_json(books)
