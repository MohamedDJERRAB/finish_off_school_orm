from sqlalchemy import create_engine ,MetaData
from sqlalchemy import text ,Column ,Integer , String , MetaData ,select ,ForeignKey,Table
from mission2 import Books 
from sqlalchemy.sql import functions

engine = create_engine("sqlite:///bibliotheque_alexandrie.db", echo=True)
with engine.connect() as conn:
    #juste un essaye : elle fonctionne pas 
    result_min_year = conn.execute(select(Books.title).where(Books.year_published == (conn.execute(select([functions.min(Books.year_published)])))))
    conn.commit()    
    for row in result_min_year:
        print(row)
