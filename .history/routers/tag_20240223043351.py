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
        
@routerTag.get('/all_tags')
async def get_tags(db:Session=Depends(get_db)):
    return crud.get_tags(db)

@routerTag.get('/tag')
async def get_tag(tag_id: int, db:Session=Depends(get_db)):
    return crud.get_tag(db, tag_id)

@routerTag.post('/add_tag')
async def create_tag(tag:schemas.TagCreate, db:Session=Depends(get_db)):
    return crud.create_tag(db, tag)

@routerTag.put('/update_tag')
async def update_tag(tag_id:int, tag_body: schemas.TagCreate, db:Session=Depends(get_db)):
    return crud.update_tag(db, tag_id, tag_body)

@routerTag.delete('/delete_tag')
async def delete_tag(tag_id:int, db:Session=Depends(get_db)):
    return crud.delete_tag(db, tag_id)