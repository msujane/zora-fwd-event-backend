from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, User
from database import engine, SessionLocal
import crud
from pydantic import BaseModel, EmailStr, Field
from fastapi.middleware.cors import CORSMiddleware
from schemas import UserResponseSchema
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Registration and Feedback API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class RegistrationSchema(BaseModel):
    name: str = Field(..., max_length=255)
    email: EmailStr
    phone: str = Field(None, max_length=20)

class ScoreSchema(BaseModel):
    email: EmailStr
    score: float

class FeedbackSchema(BaseModel):
    email: EmailStr
    feedback: str = Field(..., max_length=2000)

@app.post("/register", tags=["User"])
def register(data: RegistrationSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="User already registered with this email.")
    user = crud.create_user(db, data.name, data.email, data.phone)
    if not user:
        raise HTTPException(status_code=500, detail="Could not create user")
    return {"message": "User registered", "user_id": user.id}

@app.post("/submit-score", tags=["User"])
def submit_score(data: ScoreSchema, db: Session = Depends(get_db)):
    user = crud.update_user_score(db, data.email, data.score)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Score saved", "user_id": user.id}

@app.post("/submit-feedback", tags=["User"])
def submit_feedback(data: FeedbackSchema, db: Session = Depends(get_db)):
    user = crud.update_user_feedback(db, data.email, data.feedback)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Feedback saved", "user_id": user.id}

@app.get("/users", response_model=List[UserResponseSchema], tags=["Admin"])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/winners", response_model=List[str], tags=["Admin"])
def get_top_winners(db: Session = Depends(get_db)):
    # Order by score DESC, then by created_at ASC (oldest first)
    winners = (
        db.query(User)
        .filter(User.score != None)
        .order_by(User.score.desc(), User.created_at.asc())
        .limit(3)
        .all()
    )
    return [user.name for user in winners]