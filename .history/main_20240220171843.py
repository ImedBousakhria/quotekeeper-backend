from fastapi import FastAPI

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

