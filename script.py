# Mission one _ Master the Basics & Engine of Progress
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


database_url = 'sqlite:///library_of_alexandria.db'
#create an engine and establish a connexion with database which it would be manipulated using ORM 
engine = create_engine(database_url)

session = Session(bind=engine)


session.commit()


session.close()

