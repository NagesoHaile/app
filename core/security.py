from passlib.context import CryptContext
import os
from datetime import datetime,timedelta
from typing import Optional,Union
from jose import JWTError,jwt
from dotenv import load_dotenv
from fastapi import HTTPException,status

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET_KEY')
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed:str)->bool:
    return pwd_context.verify(plain_password,hashed)



def generate_access_token(data:dict,expires_delta:Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(days=30))
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,JWT_SECRET,algorithm=ALGORITHM)


def decode_token(token:str)->str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
          headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,JWT_SECRET,algorithms=[ALGORITHM])
        user_id: Union[int,str] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return user_id
    except JWTError:
        raise credentials_exception