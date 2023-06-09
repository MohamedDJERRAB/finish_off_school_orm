from sqlalchemy import create_engine ,MetaData

from sqlalchemy import text ,Column ,Integer , String , MetaData ,select ,ForeignKey,Table
from mission2 import Books 

from sqlalchemy.sql import functions
engine = create_engine("sqlite:///bibliotheque_alexandrie.db", echo=True)
with engine.connect() as conn:
    result = conn.execute(select(Books.category_id,Books.title).group_by(Books.category_id,Books.title))
    conn.commit()    
    for row in result:
        print(row)
    
