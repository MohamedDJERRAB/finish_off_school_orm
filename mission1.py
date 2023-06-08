# Define a 'books' table with columns id, title, author, description, and year_published. Insert five books of your choice into the 'books' table.

from  sqlalchemy import create_engine


engine = create_engine('sqlite:///Alexandria.db')

connect = engine.connect()

connect.close()