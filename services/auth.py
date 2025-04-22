from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate,UserLogin
from app.core.security import hash_password,verify_password,generate_access_token,decode_token
from fastapi import HTTPException

def register_user(db:Session,user_data:UserCreate):
    existing_user = db.exec(select(User).where(User.id == user_data.email)).first()

    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered.")
    
    new_user = User(
        email=user_data.email,
        name=user_data.name,
        password=hash_password(user_data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User registered successfully.",
            "data":new_user
            }

def login_user(db:Session,credentials:UserLogin):
    user = db.exec(select(User).where(User.email == credentials.email)).first()
    if not user or not verify_password(credentials.password,user.password):
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    
    token = generate_access_token(data={"sub":str(user.id)})
    return {"access_token":token,"token_type":"Bearer"}



