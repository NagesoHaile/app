from typing import Optional,List
import uuid 
from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title:str
    content:str


class PostRead(PostBase):
    id:uuid.UUID
    user_id:uuid.UUID
    created_at:datetime
    updated_at:datetime

class PostCreate(PostBase):
    pass 

class PostUpdate(BaseModel):
    title:Optional[str] = None
    content:Optional[str] = None

class CommentBase(BaseModel):
    content:str

class CommentRead(CommentBase):
    id:uuid.UUID
    user_id:uuid.UUID
    post_id:uuid.UUID
    created_at:datetime
    updated_at:datetime

class CommentCreate(CommentBase):
    pass 

class CommentUpdate(BaseModel):
    content:Optional[str] = None
    
