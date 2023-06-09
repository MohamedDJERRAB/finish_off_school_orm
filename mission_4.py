from sqlalchemy.orm import relationship, backref
import select
import sqlalchemy
from sqlalchemy import ForeignKey, create_engine, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Session,joinedload
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
    categories = relationship(
        "Categories", secondary="book_categories", back_populates="books"
    )
    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, author={self.author}, description={self.description}, year_published={self.year_published})"

#create categories table
class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship(
        "Book", secondary="book_categories", back_populates="categories"
    )
    def __repr__(self) -> str:
        return f"Categories(id={self.id}, name={self.name})"

# book_categorie table
class book_categories(Base):
    __tablename__ = "book_categories"
    book_id= Column(Integer, ForeignKey(Book.book_id),primary_key=True)
    category_id = Column(Integer, ForeignKey(Categories.id),primary_key=True)
    def __repr__(self) -> str:
        return f"book_categories(id={self.book_id},category_id={self.category_id})"
    
#create tables
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

#inserting  category

with Session(engine) as session:
    category = Categories(id=1,name="fiction")
    session.add(category)
    session.commit()

with Session(engine) as session:
    book_category = book_categories(book_id=520, category_id=1)  
    session.add(book_category)
    session.commit()

#list all books withis a specific category
with Session(engine) as session:
    books = session.query(Book).join(Book.categories).filter(Categories.id == 1).options(joinedload(Book.categories)).all()
    for book in books:
        print(f"Book ID: {book.book_id}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Description: {book.description}")
        print(f"Year: {book.year}")
        print("Categories:")
        for category in book.categories:
            print(f"- {category.name}")
        print("------")
        