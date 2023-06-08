from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///AlexandriaLibrary.db")
Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))
    description = Column(Text)
    year_published = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()


def retrieve_books_by_author(author):
    books = session.query(Book).filter_by(author=author).all()
    return books


def update_book_description(book_id, new_description):
    book = session.query(Book).get(book_id)
    book.description = new_description


def delete_book(book_id):
    book = session.query(Book).get(book_id)
    session.delete(book)


if __name__ == "__main__":
    books_by_author = retrieve_books_by_author("Douglas Adams")
    for book in books_by_author:
        print(
            f"Title: {book.title}, Author: {book.author}, Description: {book.description}"
        )

    update_book_description(1, "Hello world!")

    delete_book(2)

    session.commit()
    session.close()
