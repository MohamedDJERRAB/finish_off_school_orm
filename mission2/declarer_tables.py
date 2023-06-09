from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,  Integer,String,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy .orm import relationship
#mission2
Base= DeclarativeBase()

class Base(DeclarativeBase):
    pass
class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    Book_title: Mapped[str] = mapped_column(String(30))
    Book_aut : Mapped[str] =mapped_column(String(30))
    Book_year:Mapped[int] = mapped_column(Integer())
    Book_disc: Mapped[str]= mapped_column(String(30))
    #mission4
    categories = relationship("Categorie", back_populates="book")

### MISSION 4 ###
class categorie(Base):
    __tablename__ = "categorie"
    id: Mapped[int] = mapped_column(primary_key=True)
categorie_book: Mapped[str] = mapped_column(String(30))
book_id :Mapped[str]=mapped_column(Integer, ForeignKey("Book.id"))
book = relationship("Book", back_populates="categories")


engine = create_engine("sqlite:///Alexendriebiblio.db", echo=True)
Base.metadata.create_all(bind=engine)


with Session (engine) as session :


    book1 = Book(id=12345, Book_title="l'etranger",Book_aut="Albert Camus",Book_year=1948, Book_disc="/")
    book2 = Book(id=12335, Book_title="la mort dans l'ame",Book_aut="Jean Paul Sartre",Book_year=1938, Book_disc="/")
    book3 = Book(id=12385, Book_title="la peste",Book_aut="Albers Camus",Book_year=1945, Book_disc="/")
    book4 = Book(id=12355, Book_title="l'existancialisme est un humanisme",Book_aut="Jean Paul Sartre",Book_year=1962, Book_disc="/")
    book5 = Book(id=12365, Book_title="la nausée",Book_aut="Jean Paul Sartre",Book_year=1954, Book_disc="description des temps de la peste")

    session.add(book1)
    session.add(book2)
    session.add(book3)
    session.add(book4)
    session.add(book5)

    session.commit()

    ##mission3: 
    #test pour voir si ça marche 
    books=session.query(Book)
    for book in books:
        print(book.Book_title,book.Book_aut)
            
    # Recuperer les livres d'un auteur --> using orderBy
    books=session.query(Book).order_by(Book.Book_aut)
    for book in books:
        print(book.Book_title,book.Book_aut)
    
    #changer la description d'un livre
    book = session.query(Book).filter(Book.Book_aut=='Albert Camus').first()
    book.Book_disc='indiferent a sa propre vie'
    session.commit()
    print(Book.Book_aut,Book.Book_disc)
    
    
    #supprimer un livre 
books = session.query(Book).filter(Book.Book_title == "la peste").all()
for book in books:
    session.delete(book)
session.commit()

Books = session.query(Book)
for book in Books:
    print(book.Book_title, book.Book_aut)
##Mission4
with Session (engine)  as session:
    c1 = categorie(        
    id = 1111,
    categorie_book = "philosophie"
    )
    c2 = categorie(        
    id = 2222,
    categorie_book = "histoire"
    )
    
    book1.categories = c2
    book2.categories = c1
    book3.categories = c2
    book4.categories = c1
    book5.categories = c2
    
    
    session.add_all([book1,book2,book3,book4,book5])
    resultats = session.query(Book).all() 
for i in resultats:
    print(f"Titre: {i.Book_title}, Categorie: {i.categories}")