from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///AlexandriaLibrary.db", echo=True)
Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))
    description = Column(Text)
    year_published = Column(Integer)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

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

session.add_all([book1, book2, book3, book4, book5])
session.commit()

session.close()
