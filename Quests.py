#In[]

from sqlalchemy import create_engine


# creating an Engine to connect to our database, the databse is in-memory-only (temporary database)
Alexandria_library = create_engine("sqlite+pysqlite:///:memory:", echo=True)




#In[]





# %%
