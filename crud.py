import models, schemas, auth
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

# book crud
def show_books(db: Session):
    books = db.query(models.Book).all()
    return books

def get_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book :
        raise HTTPException(status_code=404, detail="Book not found" )
    return book


def create_book(db:Session, book:schemas.BookBase):
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
    

    ###################################################################    
    
# quote cruds
def get_quotes(db: Session):
    quotes = db.query(models.Quote).all()
    return quotes

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

def update_quote(db: Session, id: int , data: schemas.QuoteBase):
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

def get_bookmarked_quotes(db: Session):
    bookmarked = db.query(models.Quote).filter(models.Quote.bookmarked == True).all()
    return bookmarked
    
    
def bookmark_quote(db: Session, quote_id:int):
    db_quote = db.query(models.Quote).filter(models.Quote.id == quote_id).one_or_none()
    if db_quote is None:
        return {"error":"no such quote"}
    setattr(db_quote, "bookmarked", True)

    db.commit()
    db.refresh(db_quote)
    return {"success":f"quote '{db_quote.id}' has been bookmarked"}


def unbookmark_quote(db: Session, quote_id:int):
    db_quote = db.query(models.Quote).filter(models.Quote.id == quote_id).one_or_none()
    if db_quote is None:
        return {"error":"no such quote"}
    setattr(db_quote, "bookmarked", False)

    db.commit()
    db.refresh(db_quote)
    return {"success":f"quote '{db_quote.id}' has been bookmarked"}

def search_quotes_by_term(db: Session, term: str):
    return db.query(models.Quote).filter(
        (
            (models.Quote.quote_text.ilike(f"%{term}%")) |  # by quote text
            (models.Quote.author.ilike(f"%{term}%"))       # by author
        )
    ).all()

def get_quotes_by_book(db: Session, book_id: int):
    quotes = db.query(models.Quote).filter(models.Quote.book_id == book_id).all()
    if not quotes :
        raise HTTPException(status_code=404, detail="Quotes not found for this book" )
    return quotes

def get_quotes_by_user(db: Session, user_id: int):
    quotes = db.query(models.Quote).filter(models.Quote.user_id == user_id).all()
    if not quotes :
        raise HTTPException(status_code=404, detail="Quotes not found for this user" )
    return quotes


###################################################################

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




# user CRUDs
# User register
async def sign_up(db: Session, user: schemas.UserCreate):
    # Check if the user already exists
    existing_user = await auth.get_user_by_username(user.username, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    # Create the user in the database
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, password=hashed_password, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# User login
async def login( db: Session, username:str, pwd:str):
    user = await auth.authenticate_user(username, pwd, db)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    # Create JWT token
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "user_id": user.id, "token_type": "bearer"}

#users
def get_all_users(db: Session):
    """
    Retrieve all users from the database.
    """
    data = (db.query(models.User, models.Quote, models.Book)
            .join(models.Quote, models.User.id == models.Quote.user_id)
            .join(models.Book, models.User.id == models.Book.user_id)
            .all())
    
    user_dict = {}

    for user, quote, book in data:
        if user.id not in user_dict:
            user_dict[user.id] = {
                "user": user,
                "quotes": [],
                "books": []
            }
        user_dict[user.id]["quotes"].append(quote)
        user_dict[user.id]["books"].append(book)

    formatted_result = list(user_dict.values())
    return formatted_result