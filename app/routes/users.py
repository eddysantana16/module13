from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=user.password  # You can add real hashing later
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
