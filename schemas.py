from pydantic import BaseModel
from typing import Optional, List

# Schemas for User
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    quotes: list[Quote]=[]
    favs: list[Fav]=[]
    class config:
        orm_mode=True
        
        
# Schemas for Book
class BookBase(BaseModel):
    title: str
    author: str=Optional[str]
    image_url: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    
    class config:
        orm_mode=True
    
    
# Schemas for Quote
class QuoteBase(BaseModel):
    quote_text: str
    author: str
    image_url: str=Optional[str]


class QuoteCreate(QuoteBase):
    tags: Optional[List[str]] = None

    pass

class Quote(QuoteBase):
    id: int
    user_id: int
    book_id: int
    tags: Optional[List[str]] = None

    
    class config:
        orm_mode=True
        