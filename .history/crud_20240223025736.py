import models, schemas
from sqlalchemy.orm import Session

def show_books(db: Session):
    books = db.query(models.Book).all()
    return books

def create_book(db:Session, book:schemas.BookCreate):
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {f"a new book with id {new_book.id} has been created "}

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    book_data = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book_data:
        return {"This Book ID does not exist"}
        
    # Merge the existing data of the book with the updated fields from the user request
    for key, value in book.dict().items():
        setattr(book_data, key, value)  

    db.commit()
    return {'The book has been successfully updated'}  

def delete_book(db: Session, book_id:int): 
    book = db.query(models.Book).filter(models.Book.id==