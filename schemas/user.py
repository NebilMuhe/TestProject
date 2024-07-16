from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True
