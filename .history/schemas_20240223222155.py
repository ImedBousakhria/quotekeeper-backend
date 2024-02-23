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
# class FavBase(BaseModel):
#     user_id: int
#     quote_id: int

# class FavCreate(FavBase):
#     pass

# class Fav(FavBase):
#     id: int
    
#     class config:
#         orm_mode = True
    
    
# Schemas for Quote
class QuoteBase(BaseModel):
    quote_text: str
    author: str=Optional[str]
    image_url: str=Optional[str]
    tags: Optional[list[str]] = []



class QuoteCreate(QuoteBase):
    user_id: int
    book_id: int

class Quote(QuoteBase):
    id: int

    class config:
        orm_mode=True
        



# Schemas for Book
class BookBase(BaseModel):
    title: str
    author: str
    image_url: str=Optional[str]
    tags: Optional[List[Tag]]=[]

class BookCreate(BookBase):
    user_id: int


class Book(BookBase):
    id: int
    quotes: list[Quote]=[]
    
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
    favs: List[Fav]=[]
    books: list[Book] = []
    class config:
        orm_mode=True
        
        

