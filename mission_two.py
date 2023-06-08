from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# Define the 'books' table model
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    description = Column(Text)
    year_published = Column(Integer)

# Create the database engine and tables
engine = create_engine('sqlite:///library_of_alexandria.db')  
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert five books into the 'books' table
book1 = Book(title='Animal Farm', author='jorge orwell', description='Description 1', year_published=1945)
book2 = Book(title='The Secret', author='Rhonda Byrne', description='Description 2', year_published=2016)
book3 = Book(title='the old man and the sea', author='Ernest Hemingway', description='Description 3', year_published=1952)
book4 = Book(title='it ends with us', author='Colleen Hoover', description='Description 4', year_published=2019)
book5 = Book(title='Stranger in a strange land', author='Robert A. Heinlein', description='Description 5', year_published=2018)


session.add_all([book1, book2, book3, book4, book5])
session.commit()

# Close the session
session.close()
