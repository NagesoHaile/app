from fastapi import HTTPException,status,Request
from app.models.post import Post,Comment
from app.schemas.post import PostCreate  

from sqlmodel import Session, func,select,or_
from uuid import UUID
from typing import Optional,Union
from urllib.parse import urlencode

def create_post(db:Session,post_data:PostCreate,user_id:UUID):
    """
         Create a post
        """
    post = Post(**post_data.model_dump(),user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_all_posts(request:Request,db:Session,limit:int,page:int,search:Optional[str]):
        """
         Lists posts with pagination
        """
        query = select(Post)
        if search:
             query = query.where(or_(
                   Post.title.ilike(f"%{search}%"),
                   Post.content.ilike(f"%{search}%"),
             ))
            
        total = db.exec(select(func.count(Post.id))).one()
        posts = db.exec(query.offset(page).limit(limit)).all()
        base_url = str(request.url).split('?')[0]
        query_params = request.query_params._dict.copy()
        def build_url(new_page:int):
              query_params['page'] =str(new_page)
              return f"{base_url}?{urlencode(query_params)}"
        next_url = build_url(page +1) if (page +1) * limit <total else None
        prev_ulr = build_url(page -1) if page >0  else None

        return {
            "results": posts,
            "total": total,
            "per_page":limit,
            "page":page,
            "next":next_url,
            "prev":prev_ulr
        }
 

