from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///AlexandriaLibrary.db", echo=True)
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    books = relationship("Book", secondary="book_categories")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))
    description = Column(Text)
    year_published = Column(Integer)
    categories = relationship("Category", secondary="book_categories")


class Book_Categories(Base):
    __tablename__ = "book_categories"
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

category1 = Category(id=1, name="science")
category2 = Category(id=2, name="biology")
category3 = Category(id=3, name="math")

book1 = Book(
    title="The Hitchhiker" "s Guide to the Galaxy",
    author="Douglas Adams",
    description="A humorous science fiction novel about a man who is whisked away on an adventure through space after the Earth is destroyed.",
    year_published=1979,
)
book2 = Book(
    title="The Lord of the Rings",
    author="J.R.R. Tolkien",
    description="A fantasy novel about a hobbit named Frodo who sets out on a quest to destroy the One Ring, an evil artifact created by the Dark Lord Sauron.",
    year_published=1954,
)
book3 = Book(
    title="Harry Potter and the Sorcerer" "s Stone",
    author="J.K. Rowling",
    description="A fantasy novel about a young boy named Harry Potter who discovers that he is a wizard and attends Hogwarts School of Witchcraft and Wizardry.",
    year_published=1997,
)
book4 = Book(
    title="The Hunger Games",
    author="Suzanne Collins",
    description="A dystopian novel about a young girl named Katniss Everdeen who volunteers to take her younger sister's place in a deadly competition.",
    year_published=2008,
)
book5 = Book(
    title="The Martian",
    author="Andy Weir",
    description="A science fiction novel about an astronaut who is stranded on Mars and must use his ingenuity to survive.",
    year_published=2011,
)

book_categories1 = Book_Categories(
    book_id=1,
    category_id=1,
)
book_categories2 = Book_Categories(
    book_id=2,
    category_id=2,
)
book_categories3 = Book_Categories(
    book_id=3,
    category_id=3,
)
book_categories4 = Book_Categories(
    book_id=4,
    category_id=1,
)
book_categories5 = Book_Categories(
    book_id=5,
    category_id=3,
)


session.add_all(
    [
        category1,
        category2,
        category3,
        book1,
        book2,
        book3,
        book4,
        book5,
        book_categories1,
        book_categories2,
        book_categories3,
        book_categories4,
        book_categories5,
    ]
)
session.commit()


def list_books_by_category(category_name):
    books = (
        session.query(Book)
        .join(Book.categories)
        .filter(Category.name == category_name)
        .all()
    )

    return books


if __name__ == "__main__":
    books_by_category = list_books_by_category("math")
    for book in books_by_category:
        print(
            f"Title: {book.title}, Author: {book.author}, Description: {book.description},Category:{book.categories}"
        )
    session.close()
