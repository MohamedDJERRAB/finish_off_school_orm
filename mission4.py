from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine , select 
from mission2 import Books

engine = create_engine("sqlite+pysqlite:/// Alexandrie.db", echo=True)

with engine.connect() as conn:
        #répertorie tous les livres d'une catégorie spécifique: 
    stmt = conn.execute(select(Books.id_category,Books.title).group_by(Books.id_category,Books.title))
    conn.commit()    
    for row in stmt:
        print(row)
 
