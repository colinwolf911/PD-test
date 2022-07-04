from importlib.resources import contents
from operator import truediv
from typing import Optional
from click import option
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


#create instance 
app = FastAPI()


#define the class
class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int] = None

my_posts=[{"title":"title of post1","content":"content of post1","id":1},{"title":"checkout","content":"phone","id":2}]


@app.get("/")
async def root():
 return {"message":"welcome to personal digital online shopping "}

#retrive data
@app.get("/posts")
def get_posts():
    #return {"data": "here it's your posts."}
    return {"data": my_posts}

#request get method url "/" order impact does matter






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
#@app.post("/posts")
#def create_posts(post : Post):
 #   print(post)
 #   print(post.dict())
 #   return {"data":post}


#update data
@app.post("/posts")
def create_posts(post : Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data":post_dict}