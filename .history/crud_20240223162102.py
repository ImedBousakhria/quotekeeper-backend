import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

# book crud
def show_books(db: Session):
    books = db.query(models.Book).all()
    return books

def get_book(db: Session, book_id: int):
    quote = db.query(models.Quote).filter(models.Quote.id == book_id).first()
    if not book :
        raise HTTPException(status_code=404, detail="Quote not found" )
    return book

def create_book(db:Session, book:schemas.BookCreate):
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {f"a new book with id {new_book.id} has been created "}

def update_book(db: Session, book_id: int, book: schemas.Book):
    book_data = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book_data:
        return {"This Book ID does not exist"}
        
    updated_data = book.dict(exclude_unset=True)
    # for field, value in new_competence.model_dump(exclude_unset=True).items():
    #         setattr(db_old_competence, field, value)
    # Update only the fields provided in the updated book object
    for key, value in updated_data.items():
        setattr(book_data, key, value)

    db.commit()
    db.refresh(book_data)
    return {f'The book {book_data.id} has been successfully updated'}  


def delete_book(db: Session, book_id:int): 
    book = db.query(models.Book).filter(models.Book.id==book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return{f"The book {book.id} has been deleted"}
    else:
        return{"This Book ID does not exist."}
    
    
    
    
    
    
# quote cruds
def get_quotes(db: Session):
    quotes = db.query(models.Quote).all()
    return [quote for quote in quotes]

def create_quote(db: Session, quote: schemas.QuoteCreate):
    new_quote = models.Quote(**quote.model_dump()) 
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return {'ID of the created Quote': new_quote.id}

def get_quote(db: Session, quote_id: int):
    quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()
    if not quote :
        raise HTTPException(status_code=404, detail="Quote not found" )
    return quote

def update_quote(db: Session, id: int , data: schemas.QuoteCreate):
    quote = db.query(models.Quote).filter(models.Quote.id == id).first()
    if not quote :
        raise HTTPException(status_code=404,detail="Quote not found")
    else:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(quote, field, value)
        db.commit()
        db.refresh(quote)
    return {f"The quote {quote.id} has been updated."}

def delete_quote(db:Session, id:int):
    result = db.query(models.Quote).filter(models.Quote.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Quote not found")
    db.delete(result)
    db.commit()
    return {f"The quote {result.id} has been deleted."}




# tag cruds
def get_tags(db: Session):
    tags = db.query(models.Tag).all()
    return {"total": len(tags), "data": tags}

def create_tag(db: Session, tag: schemas.TagCreate):
    new_tag = models.Tag(**tag.dict())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return {"ID of the created Tag": new_tag.id}

def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id==tag_id).first()

def update_tag(db: Session, tag_id: int, tag: schemas.TagCreate):
    tag_data = get_tag(db, tag_id)
    if not tag_data:
        raise HTTPException(status_code=404, detail="Tag not found")
    for key, value in tag.dict().items():
        setattr(tag_data,key,value)
    db.commit()
    return {"Message":f"Updated {tag_id} Successfully"}

def delete_tag(db: Session, tag_id: int):
    data = get_tag(db, tag_id)
    if not data:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(data)
    db.commit()
    return {"Message":f"Deleted {tag_id} Successfully"}


# bookmark CRUDs
""" def get_bookmarks(db:Session):
    return db.query(models.Fav).all()

def create_bookmark(db: Session, fav:schemas.FavCreate):
    new_bm = models.Fav(**fav.dict())
    db.add(new_bm)
    db.commit()
    db.refresh(new_bm)
    return {"ID of Bookmarked Quote":new_bm}

def get_bookmark(db:Session, bmid:int):
    return db.query(models.Fav).filter(models.Fav.id == bmid).first() """
    
# better practice is to add a "bookmarked" field in the quote model

