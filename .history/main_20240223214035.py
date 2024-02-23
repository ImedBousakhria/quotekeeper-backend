from fastapi import FastAPI, Depends
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from routers.book import routerBook
from routers.quote import routerQuote
from routers.tag import routerTag
from routers.user import routerUser
# from routers.fav import routerAuthor

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
app.include_router(routerBook)
app.include_router(routerUser)
app.include_router(routerTag)
# app.include_router(routerFav)
app.include_router(routerQuote)


    