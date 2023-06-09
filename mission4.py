
import sqlalchemy 
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey,MetaData,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

engine = create_engine('sqlite:///library_of_Alexandria.db', echo=True)

Base = declarative_base()



class Category(Base):
    __tablename__ = 'categories'
    id = Column("id" ,Integer, primary_key=True)
    name = Column(String)


class books (Base):
    
    __tablename__ = 'books'
    id =Column("id",Integer, primary_key=True )
    title = Column(String)
    author=Column(String)
    description = Column(String)
    year_published=Column(Integer)
    Category= Column(Integer, ForeignKey('categories.id'))

    def __repr__(self):
        return  f"{self.id}{self.title}{self.author}{self.description}{self.year_published}{self.category}"
    