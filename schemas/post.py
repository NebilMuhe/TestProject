from pydantic import BaseModel

class PostBase(BaseModel):
    text: str

class PostCreate(PostBase):
    pass

class PostInDB(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
