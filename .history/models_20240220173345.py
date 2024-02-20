from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, unique=True, index=True)
    category = Column(String)  
    description = Column(String)
    
