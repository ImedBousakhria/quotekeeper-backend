from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.orm import relationship
import datetime

from database import Base

# Define association tables (many-to-many)
quote_tag_association = Table(
    'quote_tag_association',
    Base.metadata,
    Column('quote_id', Integer, ForeignKey('quote.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

book_tag_association = Table(
    'book_tag_association',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)
    
    books = relationship("Book", back_populates="user")
    quotes = relationship("Quote",back_populates="user")

class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    author = Column(String, nullable=, index=True)
    title = Column(String, unique=True, index=True)
    image_url = Column(String, nullable=True)

    user = relationship("User", back_populates="books")
    quotes = relationship("Quote",back_populates="book")
    tags = relationship("Tag", secondary=book_tag_association, back_populates="books")

    
class Quote(Base):
    __tablename__ = "quote"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    author = Column(String, nullable=True, index=True)
    quote_text = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    image_url = Column(String, nullable=True)
    bookmarked=Column(Boolean, default=False)

    user = relationship("User", back_populates="quotes")
    book = relationship("Book", back_populates="quotes")
    tags = relationship("Tag", secondary=quote_tag_association, back_populates="quotes")
    

class Tag(Base):
    __tablename__ = "tag"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    quotes = relationship("Quote", secondary=quote_tag_association, back_populates="tags")
    books = relationship("Book", secondary=book_tag_association, back_populates="tags")



    

