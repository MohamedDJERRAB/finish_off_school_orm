# Demonstrate your understanding by writing a Python script that creates an engine and connects it to 
# the Library of Alexandria database. Include comments to explain SQLAlchemy's core principles
# and how you have applied them in your script

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
books_data = [
    Book('Book 1', 'Author 1', 'Description 1', 2000),
    Book('Book 2', 'Author 2', 'Description 2', 1970),
    Book('Book 3', 'Author 3', 'Description 3', 1999),
    Book('Book 4', 'Author 4', 'Description 4', 2019),
    Book('Book 5', 'Author 5', 'Description 5', 2017)
]
session.add_all(books_data)
session.commit()
session.close()
