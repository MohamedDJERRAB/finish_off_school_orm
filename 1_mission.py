from sqlalchemy import create_engine


#Create the engine
engine = create_engine('sqlite:///Alexandria.db')
connection = engine.connect()
connection.close()