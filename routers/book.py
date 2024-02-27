from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal
import crud
from database import SessionLocal
import schemas

routerBook=APIRouter(
    prefix="/book",
    tags=['BOOKS']
)

def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@routerBook.get('/all_books')
async def show_books(db:Session=Depends(get_db)):
    return crud.show_books(db)

@routerBook.get('/book')
async def get_book(book_id: int, db:Session=Depends(get_db)):
    return crud.get_book(db, book_id)

@routerBook.post('/add_book')
async def create_book(book:schemas.BookCreate, db:Session=Depends(get_db)):
    return crud.create_book(db, book)

@routerBook.put('/update_book')
async def update_book(book:schemas.BookBase, id_book:int, db:Session=Depends(get_db)):
    return crud.update_book(db, id_book, book )

@routerBook.delete('/delete_book')
async def delete_book(id_book:int, db:Session=Depends(get_db)):
    return crud.delete_book(db, id_book)

@routerBook.get('/books_by_user')
async def get_books_by_user(user_id: int, db:Session=Depends(get_db)):
    return crud.get_books_by_user(db, user_id)

@routerBook.get('/search_books')
async def search_books(keyword:str, db:Session=Depends(get_db)):
    return crud.search_books_by_term(db, keyword)