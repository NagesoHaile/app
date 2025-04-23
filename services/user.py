from fastapi import HTTPException,status
from sqlmodel import Session,select
from app.models.user import User
from uuid import UUID
from app.schemas.user import UserRead


def get_current_user(db:Session,user_id:UUID):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    user = db.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise credentials_exception
    
    return {
        "ok":True,
        "data":UserRead(**user.model_dump(exclude=['password']))
    }