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
    
    # if the email already exists in the users table then it will not allow to create a new account with same email
    # if the email already exists in the users table then it will not add a new row to the table
    # and instead will return an error message saying that this email is already registered
    # otherwise it will create a new user with the provided details
    return crud.create_user(db=db,user=user)