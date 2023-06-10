from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.sql import func
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

# Query authors with the most books
Session = sessionmaker(bind=engine)
session = Session()

author_counts = session.query(Book.author, func.count(Book.author).label("book_count")).group_by(Book.author).\
    order_by(func.count(Book.author).desc()).all()

print("Authors with the most books:")
for author, book_count in author_counts:
    print("Author:", author)
    print("Book Count:", book_count)
    print()

session.close()
