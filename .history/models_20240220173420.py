from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)
    telephone=Column(String)
    rdv_pris=relationship("Rdv_pris",back_populates="client")
    ratings = relationship("Rating", back_populates="client")
    
