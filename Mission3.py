from Mission2 import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Alexandria1.db')
Session = sessionmaker(bind=engine)
session = Session()

retrieve_author = session.query().filter(Book.author == 'ghania')

for r in retrieve_author:
    print(r)

delete = session.query