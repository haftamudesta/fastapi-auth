from pydantic import BaseModel,Field
from fastapi_users import schemas
import uuid

class PostCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=200, description="Title of the post")
    content: str = Field(..., min_length=5, description="Content of the post")
    author: str = Field(..., min_length=1, max_length=50, description="Author name")
class PostResponse(BaseModel):
    title:str
    content:str
    author:str

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass