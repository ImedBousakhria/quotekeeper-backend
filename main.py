from fastapi import FastAPI
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from routers.book import routerBook
from routers.quote import routerQuote
from routers.tag import routerTag
from routers.user import routerUser

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

app.include_router(routerUser)
app.include_router(routerQuote)
app.include_router(routerBook)
app.include_router(routerTag)
