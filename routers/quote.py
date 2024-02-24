from fastapi import Body, Depends,APIRouter,Cookie,Query
from sqlalchemy.orm import Session

from database import SessionLocal,engine 
import crud
from database import SessionLocal
import schemas

routerQuote=APIRouter(
    prefix="/quote",
    tags=['QUOTES']
)

def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@routerQuote.get('/all_quotes')
async def get_quotes(db:Session=Depends(get_db)):
    return crud.get_quotes(db)

@routerQuote.get('/quote')
async def get_quote(quote_id: int, db:Session=Depends(get_db)):
    return crud.get_quote(db, quote_id)

@routerQuote.get('/quotes_by_book')
async def get_quotes_by_book(book_id: int, db:Session=Depends(get_db)):
    return crud.get_quotes_by_book(db, book_id)

@routerQuote.get('/quotes_by_user')
async def get_quotes_by_user(user_id: int, db:Session=Depends(get_db)):
    return crud.get_quotes_by_user(db, user_id)

@routerQuote.post('/add_quote')
async def create_quote(quote:schemas.QuoteCreate, db:Session=Depends(get_db)):
    return crud.create_quote(db, quote)

@routerQuote.put('/update_quote')
async def update_quote(quote_id:int, quote_body: schemas.QuoteBase, db:Session=Depends(get_db)):
    return crud.update_quote(db, quote_id, quote_body)

@routerQuote.delete('/delete_quote')
async def delete_quote(quote_id:int, db:Session=Depends(get_db)):
    return crud.delete_quote(db, quote_id)

@routerQuote.put('/bookmark_quote')
async def bookmark_quote(quote_id:int, db:Session=Depends(get_db)):
    return crud.bookmark_quote(db, quote_id)

@routerQuote.put('/unbookmark_quote')
async def unbookmark_quote(quote_id:int, db:Session=Depends(get_db)):
    return crud.unbookmark_quote(db, quote_id)

@routerQuote.get('/show_bookmarked')
async def show_bookmarked(user_id: int, db:Session=Depends(get_db)):
    return crud.get_bookmarked_quotes(db, user_id)

@routerQuote.get('/search_quotes')
async def search_quotes(keyword:str, db:Session=Depends(get_db)):
    return crud.search_quotes_by_term(db, keyword)