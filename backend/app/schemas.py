from pydantic import BaseModel,Field

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Title of the post")
    content: str = Field(..., min_length=1, description="Content of the post")
    author: str = Field(..., min_length=1, max_length=50, description="Author name")
class PostResponse(BaseModel):
    title:str
    content:str
    author:str