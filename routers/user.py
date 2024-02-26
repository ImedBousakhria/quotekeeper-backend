from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal
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
async def login(username:str,password:str,db:Session=Depends(get_db)):
    return await crud.login(db,username=username,pwd=password)
    

@routerUser.post("/register")
async def sign_up(user:schemas.UserCreate ,db:Session=Depends(get_db)):
    # if the email already exists in the users table then it will not allow to create a new account with same email
    # if the email already exists in the users table then it will not add a new row to the table
    # and instead will return an error message saying that this email is already registered
    # otherwise it will create a new user with the provided details
    return await crud.sign_up(db=db,user=user)

@routerUser.get("/users")
async def get_all_users(db: Session = Depends(get_db)):
    """
    Retrieve all users from the database.
    """
    users = crud.get_all_users(db)
    return users

@routerUser.get("/user")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by id from the database.
    """
    user = crud.get_user_by_id(db, user_id)
    return user

@routerUser.put("/user")
async def update_user(user_id: int, username: str, email:str, db: Session = Depends(get_db)):
    """
    update a user in the database.
    """
    user = crud.update_user(db, user_id, username, email)
    return user