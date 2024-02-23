from fastapi import Body, Depends,APIRouter,Cookie,Query
from sqlalchemy.orm import Session

from database import SessionLocal,engine 
import crud
from database import SessionLocal
import schemas

routerAuthor=APIRouter(
    prefix="/fav",
    tags=['FAVS']
)

def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
