from importlib.resources import contents
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

#create instance 
app = FastAPI()

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

#retrive data from body
@app.post("/createposts")
def create_posts(payload: dict= Body(...)):
    print(payload)
    return {"message":"succeefully created post"}

@app.post("/createposts")
def create_posts(payload: dict= Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']}content:{payload['content']}"}