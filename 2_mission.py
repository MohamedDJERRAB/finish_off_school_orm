
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from mission_1 import engine




#Create a session factory
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


#Define the 'books' table as a model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    description = Column(Text)
    year_published = Column(Integer)

#mission 2
#Create the database
Base.metadata.create_all(engine)

books_data = [
    {
        'title': 'Book 1',
        'author': 'Author 1',
        'description': 'Description 1',
        'year_published': 2020
    },
    {
        'title': 'Book 2',
        'author': 'Author 2',
        'description': 'Description 2',
        'year_published': 2018
    },
    {
        'title': 'Book 3',
        'author': 'Author 3',
        'description': 'Description 3',
        'year_published': 2015
    },
    {
        'title': 'Book 4',
        'author': 'Author 4',
        'description': 'Description 4',
        'year_published': 2021
    },
    {
        'title': 'Book 5',
        'author': 'Author 5',
        'description': 'Description 5',
        'year_published': 2014
    }
]

for book_data in books_data:
    book = Book(**book_data)
    session.add(book)

#Commit the changes to the database
session.commit()

#Close the session
session.close()