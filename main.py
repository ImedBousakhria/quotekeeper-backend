from fastapi import FastAPI, Depends
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


models.Base.metadata.create_all(bind=engine)

    
def get_db():
    try:
        db = SessionLocal()            
        yield db
        
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}