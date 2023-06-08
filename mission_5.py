import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///AlexandriaLibrary.db", echo=True)
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))
    description = Column(Text)
    year_published = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_oldest_books_by_category():
    subquery = (
        session.query(
            Category.id, sqlalchemy.func.min(Book.year_published).label("min_year")
        )
        .join(Book)
        .group_by(Category.id)
        .subquery()
    )
    oldest_books = (
        session.query(Book)
        .join(Category)
        .filter(
            sqlalchemy.and_(
                Category.id == subquery.c.id, Book.year_published == subquery.c.min_year
            )
        )
        .all()
    )

    return oldest_books


if __name__ == "__main__":
    oldest_books = get_oldest_books_by_category()
    for book in oldest_books:
        print(
            f"Category: {book.category.name}, Title: {book.title}, Author: {book.author}, Year Published: {book.year_published}"
        )
    session.close()
