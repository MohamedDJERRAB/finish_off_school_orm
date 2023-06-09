from sqlalchemy import create_engine ,MetaData
from sqlalchemy.orm import DeclarativeBase ,Mapped , mapped_column ,relationship
from sqlalchemy import text ,Column ,Integer , String , MetaData ,select,ForeignKey
from typing import List

meta_data = MetaData()


class Base(DeclarativeBase):
    pass
class Categories(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
         return f"Categories(id={self.id!r}, name={self.name!r})"
class Books(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(30))
    author: Mapped[str] = mapped_column(String(30))
    description:Mapped[str] = mapped_column(String(30))
    year_published:Mapped[int] 
    category_id:Mapped[str] = mapped_column(ForeignKey("categories.id"))
    def __repr__(self) -> str:
         return f"Books(id={self.id!r}, title={self.title!r}, author={self.author!r},description={self.description!r},year_published={self.year_published!r})"

engine = create_engine("sqlite:///bibliotheque_alexandrie.db", echo=True)


Base.metadata.create_all(engine)   
with engine.connect() as conn:
    conn.execute(text("insert into categories(id,name)values(:id,:name)"),[{"id":1,"name":"cat1"},{"id":2,"name":"cat2"}])
    conn.execute(text("insert into Books (id,title,author,description,year_published,category_id)values(:id,:title,:author,:description,:year_published,:category_id)"),[{"id":1,"title":"book1","author":"author1","description":"book1 de author1","year_published":1800,"category_id":1},{"id":2,"title":"book2","author":"author2","description":"book2 de author2","year_published":1960,"category_id":2},{"id":3,"title":"book3","author":"author2","description":"book3 de author2","year_published":1970,"category_id":1},{"id":4,"title":"book4","author":"author1","description":"book4 de author1","year_published":1950,"category_id":2},{"id":5,"title":"book5","author":"author3","description":"book5 de author3","year_published":1984,"category_id":1}])   
    result = conn.execute(select(Books))
   
    conn.commit()    
   
    for row in result:
        print(row)

        

