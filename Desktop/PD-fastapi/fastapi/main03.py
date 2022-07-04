from importlib.resources import contents
from operator import truediv
from telnetlib import STATUS
from typing import Optional
from click import option
from fastapi import FastAPI, Response,status,HTTPException
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
#update data
@app.post("/posts")
def create_posts(post : Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

#
#retriving from ONE individual post 
#@app.get("/posts/{id}")
#def get_post(id):
   # print(id)
   # return {"post_details":f"here is post  {id}"}

#find id 
#for p in my_posts: internation for  #if p["id"]==id;->id pass by p
def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
        

 #now call the function
##@app.get("/posts/{id}")
  
##def get_post(id):
 ##   print(type(id))
    #convert find_post id as int to match
   ## post=find_post(int(id))
    ##print(post)
   ## return {"new post-details":post}

 ##update version automative convert int
#def get_post(id):-->def get_post(id: int):
#post=find_post(int(id))-->
#@app.get("/posts/{id}")
  
#def get_post(id: int):
   # print(type(id))
    #convert find_post id as int to match
   # post=find_post(id)
   # print(post)
   # return {"new post-details":post}


#dummi app as below
@app.get("/posts/latest")
def get_latest_post():
  post=my_posts[len(my_posts)-1]
  return{"details": post}

 #pass in as paramater as reposene
#@app.get("/posts/{id}")
#def get_post(id:int,response: Response):
 #  post=find_post(id)
   ##check the post
 #  if not post:
 #   response.status_code= status.HTTP_404_NOT_FOUND
  #  return {'message':f"post with id : {id} was not found"}
  # return{"post_detail": post} 


##AUTOMATIVE PASS 
@app.get("/posts/{id}")
def get_post(id:int):
   post=find_post(id)
   #check the post
   if not post:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id : {id} was not found")
    #response.status_code= 404
    #return {'message':f"post with id : {id} was not found"}
   return{"post_detail": post} 
