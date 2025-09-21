from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class model(BaseModel):
    title: str
    body: str
    published: bool
    
@app.get("/blogs")
def read_root(limit: int, published: bool = True):
    
    return {"all blogs": "lost of all blogs"}

@app.get("/blogs/{id}")
def show_blogs(id: int):
    return {"blog_id": id}

@app.post("/create_blogs")
def create_blogs(request: model):
    return {"data": "blog is beng created"}