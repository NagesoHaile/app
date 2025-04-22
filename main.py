from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import get_session,init_db
@asynccontextmanager
async def lifespan(ap:FastAPI):
    init_db()
    yield



app = FastAPI(lifespan=lifespan)

@app.get('/')
def index():
    return {"Hello World"}