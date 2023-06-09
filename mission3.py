from sqlalchemy import create_engine , select ,text , update ,delete
from mission2 import Books
engine = create_engine("sqlite:///bibliotheque_alexandrie.db", echo=True)

with engine.connect() as conn:
    #SELECT*************************
    #result = conn.execute(text("select * from Books where author = 'author1'"))
    result = conn.execute(select(Books).where(Books.author == "author1"))
    conn.commit()    
    for row in result:
         print(row)
    #Update*************************
    conn.execute(update(Books).where(Books.id == 1).values(description  = "livre 1 de l'auteur 1 "))
    conn.commit()

    #Delete*************************
    conn.execute(delete(Books).where(Books.id == 5))
    conn.commit()    
 