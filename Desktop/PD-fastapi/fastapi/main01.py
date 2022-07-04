from importlib.resources import contents
from operator import truediv
from typing import Optional
from click import option
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

#create instance 
app = FastAPI()


#define the class
class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int] = None



@app.get("/")
async def root():
 return {"message":"welcome to my api!!!!"}

#retrive data
@app.get("/posts")
def get_posts():
    return {"data": "here it's your posts."}

#request get method url "/" order impact does matter

@app.post("/createpost")
def create_post():
    return {"post":"post is done"}



#@app.post("/createposts")
#def create_posts(payload: dict= Body(...)):
#    print(payload)
  #  return {"new_post": f"title {payload['title']}content:{payload['content']}"}


@app.post("/createposts")
def create_posts(new_post : Post):
    print(new_post.title)
    return {"data":"new post"}


#chose property as option
@app.post("/createposts01")
def create_posts(new_post : Post):
    print(new_post.published)
    return {"data":"new post"}

#optional for rating 
@app.post("/createposts02")
def create_posts(new_post : Post):
    print(new_post.rating)
    return {"data":"rating"}


#into the dictory
@app.post("/createposts03")
def create_posts(new_post : Post):
    print(new_post)
    print(new_post.dict())
    return {"data":new_post}