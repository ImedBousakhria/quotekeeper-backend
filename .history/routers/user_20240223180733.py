from fastapi import Body, Depends,APIRouter,Cookie,Query
from sqlalchemy.orm import Session

from database import SessionLocal,engine 
import crud
from database import SessionLocal
import schemas

routerUser=APIRouter(
    prefix="/user",
    tags=['USER']
)

def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@routerUser.post('/login')
async def login(username:str=Body(...),password:str=Body(...),db:Session=Depends(get_db)):
    user=crud.login(db,username=username,pwd=password)
    return user

@routerUser.post("/register")
async def sign_up(user = Body(...),db:Session=Depends(get_db)):