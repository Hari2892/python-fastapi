from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import engine, get_db

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working 🚀"}

@app.on_event("startup")
def startup():
    print("FastAPI started successfully")

# Get all users
@app.get("/users", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


# Get a single user by ID
@app.get("/user/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Create a new user
@app.post("/user/create", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# Update an existing user
@app.put("/user/update/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


# Delete a user
@app.delete("/user/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}