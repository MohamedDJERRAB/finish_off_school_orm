from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

# Define the connection string to the database
library_url = 'sqlite:///Alexandria.db'
engine = create_engine(library_url)

# Create a session factory
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
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="books")


# Define the 'categories' table as a model
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="category")


# Create the tables in the database
Base.metadata.create_all(engine)

# Function to retrieve books by category
def get_books_by_category(category_name):
    books = session.query(Book).join(Book.category).filter(Category.name == category_name).all()
    return books


# Example usage
category_name = "Science Fiction"
books_in_category = get_books_by_category(category_name)
print(f"Books in the category '{category_name}':")
for book in books_in_category:
    print(f"- {book.title}")

# Close the session
session.close()

