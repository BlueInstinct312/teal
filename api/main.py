from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated
import models as models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
#Create the tables in MYSQL DB
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_post)
    db.commit()

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id:int, db:db_dependency):
    post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return post

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post:PostBase, db:db_dependency):
    db_post = models.Posts(**post.model_dump())
    db.add(db_post)
    db.commit()

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase, db:db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id:int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@app.get("/", status_code=status.HTTP_200_OK)
async def get_page(request: Request):
    return templates.TemplateResponse("home.html", {'request': request, "name": "Home Page"})

@app.get('/data')
async def get_data(request: Request):
    return jsonable_encoder({"Key": "Password"})

#####################
# class Item(BaseModel):
#     text: str=None
#     is_done: bool=False

# items = []

# @app.get("/")
# def root():
#     return {"Hello":"World"}

# @app.post("/items")
# def create_item(item:Item):
#     items.append(item)
#     return items

# @app.get("/items/{item_id}", response_model=Item)
# def get_item(item_id:int) -> Item:
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")
