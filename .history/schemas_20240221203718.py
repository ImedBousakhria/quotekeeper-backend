from pydantic import BaseModel
from typing import Optional, List


# Tag schemas
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    
    class config:
        orm_mode = True
        


# Fav schemas
class FavBase(BaseModel):
    user_id: int
    quote_id: int

class FavCreate(FavBase):
    pass

class Fav(FavBase):
    id: int
    
    class config:
        orm_mode = True
    
    
# Schemas for Quote
class QuoteBase(BaseModel):
    quote_text: str
    author: str
    image_url: str=Optional[str]
    


class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int
    user_id: int
    book_id: int
    tags: Optional[list[Tag]] = []

    class config:
        orm_mode=True
        



# Schemas for Book
class BookBase(BaseModel):
    title: str
    author: str=Optional[str]
    image_url: str=Optional[str]
    tags: Optional[list[Tag]]=[]

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    
    class config:
        orm_mode=True
    
    
    
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
    books: list[Book] = []
    class config:
        orm_mode=True
        
        

