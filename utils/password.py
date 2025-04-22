from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprected="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed:str)->bool:
    return pwd_context.verify(plain_password,hashed)