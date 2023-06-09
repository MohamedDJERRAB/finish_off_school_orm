from mission_2 import Book
from mission_1 import engine
from mission_2 import session

retrieve_author = session.query().filter(Book.author == 'author 1')

for r in retrieve_author:
    print(r)

delete = session.query