from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List

app = FastAPI()

# In-memory user storage (like a temp database)
users_db = []

# Pydantic Model
class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr

# Add User
@app.post("/users")
def create_user(user: User):
    # Check if email already exists
    for u in users_db:
        if u['email'] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    users_db.append(user.dict())
    return {"message": "User added successfully", "user": user}

# Get all users
@app.get("/users", response_model=List[User])
def get_users():
    return users_db
