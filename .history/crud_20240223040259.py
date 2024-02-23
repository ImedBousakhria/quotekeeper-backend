import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

# book crud
def show_books(db: Session):
    books = db.query(models.Book).all()
    return books

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
        db.refresh(book_data)
    return {f"The quote {quote.id} has been updated."}

def delete_quote(db:Session, id:int):
    result = db.query(models.Quote).filter(models.Quote.id == id).delete()
    if not result.rows:
        raise HTTPException(status_code=404, detail="Quote not found")
    db.commit()
    return {f"The quote {result.id} has been deleted."}

