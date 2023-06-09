from sqlalchemy import create_engine

engine = create_engine("sqlite:///bibliotheque_alexandrie.db", echo=True)
engine.connect()