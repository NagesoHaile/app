from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel


class UserBase(BaseModel):
    name:str
    email:str


class UserCreate(UserBase):
    password:str

class UserLogin(BaseModel):
    email:str
    password:str


class UserRead(UserBase):
    id:uuid.UUID
    created_at:datetime
    updated_at:datetime

class UserUpdate(BaseModel):
    name:Optional[str] = None
    password:Optional[str] = None

