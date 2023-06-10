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

# Query authors with books across multiple genres
Session = sessionmaker(bind=engine)
session = Session()

author_genre_counts = session.query(Book.author, func.count(Category.name.distinct()).label("genre_count")).\
    select_from(Book).join(BookCategory).join(Category).group_by(Book.author).subquery()

authors_multiple_genres = session.query(author_genre_counts.c.author).filter(author_genre_counts.c.genre_count > 1).all()

print("Authors who have written books across multiple genres:")
for author in authors_multiple_genres:
    print("Author:", author[0])
    
session.close()
