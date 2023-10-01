from modules.csv import takeBooks
from modules.json import genJson

books = takeBooks()
genJson(books)
