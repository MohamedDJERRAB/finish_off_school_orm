from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from Mission1 import engine

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    year_published = Column(Integer)
    categories = relationship("Category", secondary="book_categories", back_populates="books")

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary="book_categories", back_populates="categories")

class BookCategory(Base):
    __tablename__ = "book_categories"
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)

Base.metadata.create_all(bind=engine)

# Query the oldest book in each category
Session = sessionmaker(bind=engine)
session = Session()

categories = session.query(Category).all()

for category in categories:
    oldest_book = session.query(Book).filter(Book.categories.contains(category)).order_by(Book.year_published).first()

    if oldest_book:
        print(f"Oldest book in the '{category.name}' category:")
        print("Title:", oldest_book.title)
        print("Author:", oldest_book.author)
        print("Description:", oldest_book.description)
        print("Year Published:", oldest_book.year_published)
        print()
    else:
        print(f"No books found in the '{category.name}' category.")

session.close()
