from importlib.resources import contents
from operator import truediv
from telnetlib import STATUS
from typing import Optional
from urllib import response
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

#class UpdatePost()

my_posts=[{"title":"title of post1","content":"content of post1","id":1},{"title":"checkout","content":"phone","id":2}]


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

#Delete post
def find_index_post(id):
    for i ,p in enumerate(my_posts):
        if p['id']==id:
            return i


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


#delete post
#@app.delete("/posts/{id}")
#update status
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index =find_index_post(id)
    
    #catch the error
    if index== None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"post with id  : {id} doesn't exist")

    my_posts.pop(index)
   # return {'message':'post delete'}
#no eorrer and data come back
    return Response(status_code=status.HTTP_204_NO_CONTENT)




    #####update
@app.put("/posts/{id}")
def update_post(id: int, post : Post):
    #because we receive from the front
    #we create schme such as a class
    print (post)
    index = find_index_post(id)
    #return {'message': "updated post"}

    ##find the index which has been updated
    if index== None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"post with id  : {id} doesn't exist")
    #get the post and convert it to dictory
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {"data": post_dict}


    



