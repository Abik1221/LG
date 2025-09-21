from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class model(BaseModel):
    pass

app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/blogs?limit={linit}&published={published}")
async def read_root(linit: int, published: bool = True):
    return {"all blogs": "lost of all blogs"}


app.get("/blogs/{id}")
def show_blogs(id: int):
    return {"blog_id": id}

@app.post("/create_blogs")
def create_blogs(request: model):
    return {"data": "blog is beng created"}