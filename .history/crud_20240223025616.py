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

