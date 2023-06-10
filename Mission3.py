from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Mission2 import Book

# Create an engine and bind it to a session
engine = create_engine('sqlite:///Alexandria.db')
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve all books written by a specific author
author = 'ghania'
books = session.query(Book).filter(Book.author == author).all()

# Print the retrieved books
for book in books:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Description: {book.description}")
    print(f"Year Published: {book.year_published}")
    print()

# Update a book's description
book_to_update = session.query(Book).filter(Book.title == 'Bombe').first()
if book_to_update:
    book_to_update.description = 'New Description'
    session.commit()

# Delete a book from the database
book_to_delete = session.query(Book).filter(Book.title == 'Cryptanalysis').first()
if book_to_delete:
    session.delete(book_to_delete)
    session.commit()

# Close the session
session.close()
