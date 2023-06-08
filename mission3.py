from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///Alexandria.db')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    year_published = Column(Integer)

    def __init__(self, title, author, description, year_published):
        self.title = title
        self.author = author
        self.description = description
        self.year_published = year_published

Base.metadata.create_all(engine)

def retrieve_books_by_author(author):
    books = session.query(Book).filter_by(author=author).all()
    return books

def update_book_description(book_id, new_description):
    book = session.query(Book).get(book_id)
    if book:
        book.description = new_description
        session.commit()

def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()

author = 'Author 1'
books_by_author = retrieve_books_by_author(author)
print("Books by", author)
for book in books_by_author:
    print(book.title)

book_id = 2
new_description = 'Updated description'
update_book_description(book_id, new_description)
print("Book", book_id, "description updated")

book_id = 3
delete_book(book_id)
print("Book", book_id, "deleted")

session.close()
