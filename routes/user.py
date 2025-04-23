from fastapi import APIRouter,Depends,Request
from sqlmodel import Session
from app.services.user import get_current_user
from app.config.database import get_session

router = APIRouter(prefix="/users",tags=["Users"])

@router.get('/me')
def current_user(request:Request,db:Session = Depends(get_session)):
    user_id = request.state.id
    user =  get_current_user(db=db,user_id=user_id)
    return user