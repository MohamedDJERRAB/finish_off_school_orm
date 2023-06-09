import select
import sqlalchemy
from sqlalchemy import create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import sessionmaker
from mission_3 import delete_book,update_book,select_book_author

#create a new databse data
engine = create_engine('sqlite:///alexandria.db', echo=True)


#create Alexandria database 
Base = declarative_base()


#add book table
class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    author= Column(String)
    title = Column(String)
    description= Column(String)
    year=Column(Integer)

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, author={self.author}, description={self.description}, year_published={self.year_published})"


Base.metadata.create_all(engine)


#inserting 5 books
with Session(engine) as session:
    session.execute(
        insert(Book),
        [
            {"book_id":521,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":522,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":520,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":50,"author":"Laura Mitchell","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
            {"book_id":16,"author":"Laura","title":"The Secret Garden of Dreams","description":"A heartwarming tale about a young girl who discovers a magical garden that brings hope and healing to all who enter.","year":2009},
        ],
    )
    session.commit()

#select book author
with Session(engine) as session:
    select_book_author(session,Book,"Laura")

#delete book
with Session(engine) as session:
    delete_book(session,Book,16)

#update Book
with Session(engine) as session:
    update_book(session,Book,50,"new Description")

