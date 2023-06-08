# The engine is a factory that create new db connections

from sqlalchemy import create_engine
engine = create_engine("sqlite:///alexandria.db", echo=True)