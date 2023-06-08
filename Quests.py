#In[]
from sqlalchemy import create_engine, select
from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship


#In[]

# creating an Engine to connect to our database, the databse is in-memory-only (temporary database)
Alexandria_library = create_engine("sqlite+pysqlite:///:memory:", echo=True)


class Base(DeclarativeBase):
    pass


#In[]

# defining the 'books' table
class Books(Base):
    __tablename__ = "books"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[Optional[str]]
    author : Mapped[Optional[str]]
    description : Mapped[Optional[str]]
    year_published : Mapped[Optional[int]]

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, author={self.author}, description={self.description}, year_published={self.year_published})"


#In[]

# creating our table
Base.metadata.create_all(Alexandria_library)


#In[]

# Inserting books, using Session in context manager to have it closed after execution
with Session(Alexandria_library) as session:
    b1 = Books(title="one thousand and one nights", description="A thousand and one tales, describing new fictional caracters in each one", year_published=1450)
    b2 = Books(title="The hound of the baskervills", author="Arthur Konan Doyle", description="Sherlock Holmes takes a case where the killer is believed to be an infernal hound that haunts the Baskervills family", year_published=1950)
    b3 = Books(title="The Lord of the Rings", author="J. R. R. Tolkien", description="the journey of a hero to destroy the rings", year_published=1923)
    b4 = Books(title="A Tale of Two Cities", author="Charles Dickens", year_published=1953)
    b5 = Books(title="Sahih Al Boukhari", author="Al Boukhari", description="A compilation of Hadiths and their explanation, verified by the author")

    session.add_all([b1, b2, b3, b4, b5])
    session.commit()



#In[]

# selecting a book by its author name
with Session(Alexandria_library) as session:
    stmnt = select(Books).where(Books.author.is_("Al Boukhari"))
    for res in session.scalars(stmnt):
        print(res)
        pass

#In[]
# changing a book's description
with Session(Alexandria_library) as session:
    stmnt = select(Books).where(Books.author.is_("J. R. R. Tolkien"))
    LR = session.scalars(stmnt).one()

    LR.description = "A classical sword & magic Adventure, turned into a fan favorite movie series"
    session.commit()


#In[]
# deleting a book
with Session(Alexandria_library) as session:
    stmnt = select(Books).where(Books.author.is_("Charles Dickens"))
    Tale_of_two_cities = session.scalars(stmnt).one()
    session.delete(Tale_of_two_cities)
    session.commit()




# %%
