from fastapi import HTTPException,Request
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from app.config.database import get_session
from app.utils.auth import decode_token

class AuthMiddleware(HTTPBearer):
    def __init__(self,auto_error:bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request:Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)


        if not credentials:
            raise HTTPException(
                status_code=401,detail="Authorization token missing"
            )
        try:
            user_id =decode_token(credentials.credentials)
        except Exception:
            raise HTTPException(
                status_code=401, 
                detail="Invalid token or token has expired"
            )
        request.state.id = user_id