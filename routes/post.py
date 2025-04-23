from fastapi import APIRouter,Depends,HTTPException,Request,Query
from sqlmodel import Session
from typing import List,Optional
from app.schemas.post import PostCreate,PostRead
from app.services.post import get_all_posts,create_post
from app.config.database import get_session
from app.core.middleware import AuthMiddleware
router = APIRouter(prefix="/posts",tags=['Posts'],dependencies=[Depends(AuthMiddleware())])

@router.post('')
def create_new_post(request:Request,post:PostCreate,db:Session = Depends(get_session)):
    user_id = request.state.id
    result = create_post(db=db,post_data=post,user_id=user_id)
    return result

@router.get('')
def list_posts(
    request:Request,
    db:Session = Depends(get_session),
    page: int = 0,
    per_page: int = Query(default=10,le=100),
    search:Optional[str] = Query(default=None,description="Search keywords"),
    ):
    data = get_all_posts(request=request,db=db,limit=per_page,page=page,search=search)
    return data


