# from fastapi import Body, Depends,APIRouter,Cookie,Query
# from sqlalchemy.orm import Session

# from database import SessionLocal,engine 
# import crud
# from database import SessionLocal
# import schemas

# routerFav=APIRouter(
#     prefix="/fav",
#     tags=['FAVS']
# )

# def get_db():
#     db=SessionLocal()
#     try: 
#         yield db
#     finally:
#         db.close()
        
# @routerFav.get('/all_favs')
# async def show_favs():
#     pass

# @routerFav.post('/add_fav')
# async def create_fav():
#     pass

# @routerFav.delete('/delete_fav')
# async def delete_fav():
#     pass