import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = create_engine("sqlite:///AlexandriaLibrary.db", echo=True)
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
def find_authors_with_most_books():


    authors = (
        session.query(Book.author, func.count(Book.id))
        .group_by(Book.author)
        .order_by(func.count(Book.id).desc())
        .all()
    )

    session.close()

    return authors



if __name__ == "__main__":
    author_counts = find_authors_with_most_books()
    for author, count in author_counts:
        print(f"Author: {author}, Book Count: {count}")
