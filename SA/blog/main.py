from fastapi import FastAPI
from schemas import Blog

app = FastAPI()

@app.post("/blog")
def create_blog(Blog: Blog):
    return {"message": "cthe blog is being created"}

