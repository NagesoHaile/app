
# E.S.S.I
# 1. create engine
# 2. define [get_session] method
# 3. create schema,-> means give that created
# engine into the create_all of the SQLModel.metadata function
# 4.  create init function  -> init_db()


import os
from dotenv import load_dotenv
from sqlmodel import SQLModel,create_engine,Session

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL,echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)