from fastapi import FastAPI, D
from pydantic import BaseModel, Field
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine

app = FastAPI()



models.Base.metadata.create_all(bind=engine)

    
def get_db():
    try:
        db = SessionLocal()            
        yield db
        
    finally:
        db.close()

    
    
    
class Item(BaseModel):
    name: str = Field(min_length=1)
    category:str = Field(min_length=1) 
    description: str = Field(min_length=1)




@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/todos", tags=['TODOS'])
async def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Items).all()

@app.post("/todos/add_todo", tags=['TODOS'])
async def add_todo(todo: Item, db: Session = Depends(get_db)):