from fastapi import Body, Depends,APIRouter,Cookie,Query
from sqlalchemy.orm import Session

from database import SessionLocal,engine 
import crud
from database import SessionLocal
import schemas

routerTag=APIRouter(
    prefix="/tag",
    tags=['TAGS']
)

def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@routerTag.get('/all_quotes')
async def get_quotes(db:Session=Depends(get_db)):
    return crud.get_quotes(db)

@routerTag.get('/quote')
async def get_quote(quote_id: int, db:Session=Depends(get_db)):
    return crud.get_quote(db, quote_id)

@routerTag.post('/add_quote')
async def create_quote(quote:schemas.QuoteCreate, db:Session=Depends(get_db)):
    return crud.create_quote(db, quote)

@routerTag.put('/update_quote')
async def update_quote(quote_id:int, quote_body: schemas.QuoteCreate, db:Session=Depends(get_db)):
    return crud.update_quote(db, quote_id, quote_body)

@routerTag.delete('/delete_quote')
async def delete_quote(quote_id:int, db:Session=Depends(get_db)):
    return crud.delete_quote(db, quote_id)