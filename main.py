from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel


# Pydantic Model for Blog
class Blog(BaseModel):
    title: str
    content: str


client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

app = FastAPI()


@app.post("/blog")
async def create_blog(blog: Blog):
    # Add blog to MongoDB
    db.blogs.insert_one(blog.dict())
    return {"message": "Blog added successfully"}


@app.get("/")
async def read_root():
    return {"Hello": "World"}
