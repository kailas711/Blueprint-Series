from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

test_posts = {1:{"title": "New Post", "content":"cool test post"}}

@app.get("Hello-world")
def hello_world():
    return {"message": "Hello World!!!"}

@app.get("/posts")
def get_all_posts():
    return test_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in test_posts.keys():
        raise HTTPException(status_code=404, detail="Post not found")
    return test_posts.get(id)

@app.post("/posts")
def create_posts(post:PostCreate):
    new_post = {"title": post.title, "content": post.content}
    test_posts[max(test_posts.keys())+1] = new_post
    return new_post