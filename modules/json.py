import json
from files import JSON_FILE_PATH


with open(JSON_FILE_PATH, "r") as f:
    users = json.loads(f.read())


def gen_json(books):
	books_count = len(books)
	user_count = len(users)
	booksforone = books_count // user_count
	remaining_books = books_count % user_count

	last_index = 0
	data = []

	for user in users:
		bbooks = []
		for i in range(booksforone):
			bbooks.append(books[last_index])
			last_index += 1

		if remaining_books > 0:
			bbooks.append(books[last_index])
			last_index += 1
			remaining_books -= 1

		usr_json = {
			"name": user["name"],
			"gender": user["gender"],
			"address": user["address"],
			"age": user["age"],
			"books": bbooks
		}
		data.append(usr_json)

	with open("result.json", "w") as f:
		s = json.dumps(data, indent=4)
		f.write(s)


