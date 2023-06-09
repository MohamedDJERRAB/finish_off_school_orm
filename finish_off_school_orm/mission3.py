from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the connection string to the database
database_url = 'sqlite:///Alexandria.db'

# Create the engine and session
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for declarative models
Base = declarative_base()


# Define the 'books' table as a model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    description = Column(Text)
    year_published = Column(Integer)


# Function to retrieve books by an author
def get_books_by_author(author):
    books = session.query(Book).filter(Book.author == author).all()
    return books


# Function to update a book's description
def update_book_description(book_id, description):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.description = description
        session.commit()
        print("Book description updated successfully.")
    else:
        print("Book not found.")


# Function to delete a book
def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully.")
    else:
        print("Book not found.")


# Retrieve books by author
author = "Author 1"
books_by_author = get_books_by_author(author)
print(f"Books written by {author}:")
for book in books_by_author:
    print(f"- {book.title}")

# Update book description
book_id = 1
new_description = "Updated description for Book 1"
update_book_description(book_id, new_description)

# Delete a book
book_id = 3
delete_book(book_id)

# Close the session
session.close()
