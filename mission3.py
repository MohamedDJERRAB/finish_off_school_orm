from sqlalchemy import create_engine, text, select , update , delete
from mission2 import Books

engine = create_engine("sqlite+pysqlite:/// Alexandrie.db", echo=True)

with engine.connect() as conn:
        # selection des livres qui sont écrits par l'athor "auteur":
    stmt = conn.execute(select(Books).where(Books.author== "auteur"))

        #update de la description de livre numéro 2 :
    conn.execute(update(Books).where(Books.id==2).values(description=" la nouvelle description"))
    conn.commit()

        #suppression de livre numéro 5 :
    conn.execute(delete(Books).where(Books.id==5))
    conn.commit()

    stmt = conn.execute(text("Select * from Books"))
    for row in stmt:
        print(row)

