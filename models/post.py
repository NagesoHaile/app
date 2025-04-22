from sqlmodel import SQLModel,Field,Relationship

from typing import Optional,List
from datetime import datetime
import uuid
from app.models.user import User

class Post(SQLModel,table=True):
    __tablename__ = 'posts'

    id: uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True)
    title:str
    content:str
    user_id:uuid.UUID = Field(foreign_key="user.id")
    author: Optional[User] = Relationship(back_populates="posts")
    comments: List["Comment"] = Relationship(back_populates="post")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Comment(SQLModel,table=True):
    id:uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    post_id: uuid.UUID = Field(foreign_key="post.id")
    author: Optional[User] = Relationship(back_populates="comments")
    post:Optional[Post] = Relationship(back_populates="comments")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


