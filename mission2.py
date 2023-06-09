from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import text
from sqlalchemy import create_engine , select 

class Base(DeclarativeBase):
    pass

    # creation de la table categories :
class Categories(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(30))
    def __repr__(self) -> str:
        return f"Categories(id={self.id!r}, name={self.name!r})"

    # creation de la table books : 

class Books(Base):
    __tablename__ = "books"
    id : Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    author : Mapped[str] = mapped_column(String(30))
    description : Mapped[str] = mapped_column(String(30))
    year_published: Mapped[int] 
    id_category:Mapped[str] = mapped_column(ForeignKey("categories.id"))

    def __repr__(self) -> str:
        return f"Books(id={self.id!r}, title={self.title!r}, author={self.author!r}, description={self.description!r}, year_published={self.year_published!r}, id_category={self.id_category})"

    #connexion à la base de donnée : 
engine = create_engine("sqlite+pysqlite:/// Alexandrie.db", echo=True)
Base.metadata.create_all(engine)

        #remplissage de la table categorie et book :
with engine.connect() as conn:
    conn.execute(text("insert into categories(id,name) values (:id,:name)"),[{"id":2,"name":"categorie_2"},{"id":3,"name":"categories_3"}])
    result = conn.execute(text("INSERT INTO Books (id, title, author, description, year_published, id_category) VALUES (:id,  :title,  :author,  :description, :year_published, :id_category)"),[{"id":1,  "title":'book',  "author":'auteur',  "description":'livre1',   "year_published":1980 , "id_category":2},  {"id":2,  "title":'book2',  "author":'auteur',  "description":'livre2',   "year_published":1990 , "id_category":3},{"id":3,  "title":'book3',  "author":'auteur3',  "description":'livre3',   "year_published":2000, "id_category":2},{"id":4,  "title":'book4',  "author":'auteur4',  "description":'livre4',   "year_published":2005, "id_category":3}, {"id":5,  "title":'book5',  "author":'auteur5',  "description":'livre5',   "year_published":2009 , "id_category":3}])
    result = conn.execute(text("Select * from Books"))
    conn.commit()        #valider les insertions 
    for row in result :           #Pour confirmer que l'insertion est bien faite
        print(row)
   
  


    