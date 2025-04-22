from fastapi import APIRouter,Depends
from sqlmodel import Session
from app.config.database import get_session
from app.schemas.user import UserCreate,UserLogin
from app.services.auth import register_user,login_user


router = APIRouter(prefix="/auth")

@router.post('/register')
def register(user:UserCreate,db:Session = Depends(get_session)):
    return register_user(db=db,user_data=user)

@router.post('/login')
def login(credentials:UserLogin,db:Session = Depends(get_session)):
    return login_user(db=db,credentials=credentials)

