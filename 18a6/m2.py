""" Models form the structures:
(declarative mappings: python object model -> database metadata)
which will be queryed from the database (books for our mission)

That metadata will serve as input along with the engine to create tables
"""

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from m1 import engine

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(500))
    year_published: Mapped[str] = mapped_column(String(4))

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, Title={self.title!r}, Author={self.author!r}, Description={self.description!r}, Year published={self.year_published!r})"
    
class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, Name={self.name!r})"
    
# class BookCategory(Base):
#     __tablename__ = "book categories"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     book_id: Mapped[int] = mapped_column(ForeignKey(Book.id))
#     category_id: Mapped[int] = mapped_column(Category.id)
#     def __repr__(self) -> str:
#         return f"Book category(book id={self.book_id!r}, category id={self.category_id!r})"
    
Base.metadata.create_all(engine)

"""Now inserting data in the database by creating instances of Book which have an `__init__()` method as established automatically by the declarative mapping process.
We then pass them to the database using an object called a `Session`, which makes use of the Engine to interact with the database.
"""

from sqlalchemy.orm import Session

with Session(engine) as session:
    book1 = Book(
        id = 0,
        title="Gödel, Escher, Bach: an Eternal Golden Braid",
        author="Douglas Hofstadter",
        description="Gödel, Escher, Bach: an Eternal Golden Braid, also known as GEB, is a 1979 book by Douglas Hofstadter. By exploring common themes in the lives and works of logician Kurt Gödel, artist M. C. Escher, and composer Johann Sebastian Bach, the book expounds concepts fundamental to mathematics, symmetry, and intelligence.",
        year_published ="1979"
    )
    book2 = Book(
        id = 1,
        title="Gödel, Escher, Bach: an Eternal Golden Braid",
        author="Douglas Hofstadter",
        description="Gödel, Escher, Bach: an Eternal Golden Braid, also known as GEB, is a 1979 book by Douglas Hofstadter. By exploring common themes in the lives and works of logician Kurt Gödel, artist M. C. Escher, and composer Johann Sebastian Bach, the book expounds concepts fundamental to mathematics, symmetry, and intelligence.",
        year_published ="1979"
    )
    book3 = Book(
        id = 2,
        title="Gödel, Escher, Bach: an Eternal Golden Braid",
        author="Douglas Hofstadter",
        description="Gödel, Escher, Bach: an Eternal Golden Braid, also known as GEB, is a 1979 book by Douglas Hofstadter. By exploring common themes in the lives and works of logician Kurt Gödel, artist M. C. Escher, and composer Johann Sebastian Bach, the book expounds concepts fundamental to mathematics, symmetry, and intelligence.",
        year_published ="1979"
    )
    book4 = Book(
        id = 3,
        title="Gödel, Escher, Bach: an Eternal Golden Braid",
        author="Douglas Hofstadter",
        description="Gödel, Escher, Bach: an Eternal Golden Braid, also known as GEB, is a 1979 book by Douglas Hofstadter. By exploring common themes in the lives and works of logician Kurt Gödel, artist M. C. Escher, and composer Johann Sebastian Bach, the book expounds concepts fundamental to mathematics, symmetry, and intelligence.",
        year_published ="1979"
    )
    book5 = Book(
        id = 4,
        title="Gödel, Escher, Bach: an Eternal Golden Braid",
        author="Douglas Hofstadter",
        description="Gödel, Escher, Bach: an Eternal Golden Braid, also known as GEB, is a 1979 book by Douglas Hofstadter. By exploring common themes in the lives and works of logician Kurt Gödel, artist M. C. Escher, and composer Johann Sebastian Bach, the book expounds concepts fundamental to mathematics, symmetry, and intelligence.",
        year_published ="1979"
    )
    category1 = Category(
        id = 0,
        name = "fiction"
    )
    category2 = Category(
        id = 1,
        name = "logic"
    )
    # book_category1 = BookCategory(
    #     id = 0,
    #     book_id = 0,
    #     category_id = 1
    # )
    # book_category2 = BookCategory(
    #     id = 0,
    #     book_id = 0,
    #     category_id = 1
    # )

    books = session.add_all([book1, book2, book3, book4, book5])
    session.commit()

    categories = session.add_all([category1, category2])
    session.commit()

    # book_categories = session.add_all([book_category1])
    # session.commit()