from fastapi import Body, Depends,APIRouter,Cookie,Query
from sqlalchemy.orm import Session

from database import SessionLocal,engine 
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

@routerQuote.get('/quote')
async def get_quote(quote_id: int, db:Session=Depends(get_db)):
    return crud.get_quote(db, quote_id)

@routerBook.post('/add_book')
async def create_book(book:schemas.BookCreate, db:Session=Depends(get_db)):
    return crud.create_book(db, book)

@routerBook.put('/update_book')
async def update_book(book:schemas.BookCreate, id_book:int, db:Session=Depends(get_db)):
    return crud.update_book(db, id_book, book )

@routerBook.delete('/delete_book')
async def delete_book(id_book:int, db:Session=Depends(get_db)):
    return crud.delete_book(db, id_book)