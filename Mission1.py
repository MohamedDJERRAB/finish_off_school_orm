from sqlalchemy import create_engine

# Creating a connection to Alexandria.db
engine = create_engine("sqlite:///Alexandria.db")
