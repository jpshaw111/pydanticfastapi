from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    age:int = Field(..., gt=0, lt=100)
    email: EmailStr


class UserOut(UserCreate):
    id: int


    class Config:
        orm_mode = True
