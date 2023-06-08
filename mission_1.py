import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("sqlite:///AlexandriaLibrary.db")
conn = engine.connect()
conn.close()
