from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

# Create tables in DB
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Create User
@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check duplicate
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# GET: List Users
@app.get("/users", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

#PUT: User Update
@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, updated_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if new email already exists in another user
    existing_email_user = db.query(models.User).filter(models.User.email == updated_data.email, models.User.id != user_id).first()
    if existing_email_user:
        raise HTTPException(status_code=400, detail="Email already taken")

    user.name = updated_data.name
    user.age = updated_data.age
    user.email = updated_data.email

    db.commit()
    db.refresh(user)
    return user


# DELETE: User Delete
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

