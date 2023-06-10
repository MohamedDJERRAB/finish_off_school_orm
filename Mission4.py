from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
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

b1 = Book(title="fos", author="ghania", description="finish off school", year_published=2023)
b2 = Book(title="University and work on computability", author="alan turing", description=" where Turing was an undergraduate in 1931 and became a Fellow in 1935. The computer room is named after him.", year_published=1934)
b3 = Book(title="Cryptanalysis", author="alan turing", description="Two cottages in the stable yard at Bletchley Park. Turing worked here in 1939 and 1940, before moving to Hut 8.", year_published=1938)
b4 = Book(title="Bombe", author="alan turing", description="A working replica of a bombe now at The National Museum of Computing on Bletchley Park", year_published=1940)
b5 = Book(title="Hut 8 and the naval Enigma", author="alan turing", description="Statue of Turing holding an Enigma machine by Stephen Kettle at Bletchley Park, commissioned by Sidney Frank, built from half a million pieces of Welsh slate", year_published=1942)

Session = sessionmaker(bind=engine)
session = Session()
session.add_all([b1, b2, b3, b4, b5])

# Create a 'Fantasy' category and associate the books with it
fantasy_category = Category(name='Fantasy')
fantasy_category.books.extend([b1, b2, b3, b4, b5])

session.add(fantasy_category)
session.commit()

# Query books in the 'Fantasy' category
category_name = 'Fantasy'
category = session.query(Category).filter_by(name=category_name).first()

if category:
    books = category.books

    print(f"Books in the '{category_name}' category:")
    for book in books:
        print("Title:", book.title)
        print("Author:", book.author)
        print("Description:", book.description)
        print("Year Published:", book.year_published)
        print()
else:
    print(f"No category found with the name '{category_name}'.")

session.close()
