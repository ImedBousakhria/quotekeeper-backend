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


@routerQuote.post('/add_quote')
async def create_quote(quote:schemas.QuoteCreate, db:Session=Depends(get_db)):
    return crud.create_quote(db, quote)

@routerQuote.put('/update_quote')
async def update_quote():
    pass

@routerQuote.delete('/delete_quote')
async def delete_quote():
    pass