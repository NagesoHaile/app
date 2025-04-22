from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List
from datetime import datetime
import uuid

class User(SQLModel,table=True):
    __tablename__ = 'users'
    id:uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True)
    name:str
    email:str = Field(unique=True)
    password:str
    created_at:datetime = Field(default_factory=datetime.now)
    updated_at:datetime = Field(default_factory=datetime.now)

    posts:List["Post"] = Relationship(back_populates='author')
    comments: List["Comment"] = Relationship(back_populates='author')
