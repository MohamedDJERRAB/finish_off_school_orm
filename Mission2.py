from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Mission1 import engine

# The Library of Alexandria & Filling the Shelves

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    year_published = Column(Integer)

    def __init__(self, id, title, author, description, year_published):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.year_published = year_published

    def __repr__(self):
        return f"({self.id})({self.title})({self.author})({self.description})({self.year_published})"


Base.metadata.create_all(bind=engine)

b1 = Book(id=123, title="fos", author="ghania", description="finish off school", year_published=2023)
b2 = Book(id=321, title="University and work on computability", author="alan turing", description=" where Turing was an undergraduate in 1931 and became a Fellow in 1935. The computer room is named after him.", year_published=1934)
b3 = Book(id=456, title="Cryptanalysis", author="alan turing", description="Two cottages in the stable yard at Bletchley Park. Turing worked here in 1939 and 1940, before moving to Hut 8.", year_published=1938)
b4 = Book(id=654, title="Bombe", author="alan turing", description="A working replica of a bombe now at The National Museum of Computing on Bletchley Park", year_published=1940)
b5 = Book(id=789, title="Hut 8 and the naval Enigma", author="alan turing", description="Statue of Turing holding an Enigma machine by Stephen Kettle at Bletchley Park, commissioned by Sidney Frank, built from half a million pieces of Welsh slate", year_published=1942)

Session = sessionmaker(bind=engine)
session = Session()
session.add_all([b1, b2, b3, b4, b5])
session.commit()
session.close()
