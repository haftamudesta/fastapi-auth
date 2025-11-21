from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate

app=FastAPI()

text_posts = {
    1: {
        "title": "Welcome to My Blog",
        "content": "This is my first post on this amazing platform. I'm excited to share my thoughts with you all!",
        "author": "john_doe"
    },
    2: {
        "title": "The Beauty of Python",
        "content": "Python is such a versatile language. From web development to data science, it does it all with elegance and simplicity.",
        "author": "python_lover"
    },
    3: {
        "title": "FastAPI Tips and Tricks",
        "content": "Here are some cool features of FastAPI that make API development a breeze: automatic docs, type hints, and async support!",
        "author": "api_master"
    },
    4: {
        "title": "My Travel Adventures",
        "content": "Just returned from an amazing trip to Japan. The food, culture, and people were absolutely incredible!",
        "author": "travel_bug"
    },
    5: {
        "title": "Learning FastAPI",
        "content": "Started learning FastAPI this week and I'm already building REST APIs faster than ever before. The automatic interactive documentation is a game-changer!",
        "author": "coding_novice"
    }
}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[id]
@app.post("/posts")
def create_post(post:PostCreate):
    new_post={"title":post.title,"content":post.content,"author":post.author}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post

