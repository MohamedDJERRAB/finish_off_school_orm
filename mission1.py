import sqlite3 , sqlalchemy 
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker


engine = create_engine('sqlite:///library_of_Alexandria.db', echo=True)
connexion=engine.connect()  

connexion.close()   
