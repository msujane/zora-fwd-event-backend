from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from .. import crud, schemas

router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get-random", response_model=List[schemas.QuestionOut])
def get_random_questions(count: int = 5, db: Session = Depends(get_db)):
    return crud.get_random_questions(db, count)