from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from .. import crud, schemas

router = APIRouter(
    prefix="/attempts",
    tags=["attempts"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit", response_model=schemas.AttemptOut)
def submit_attempt(attempt: schemas.AttemptCreate, db: Session = Depends(get_db)):
    return crud.create_attempt(db, attempt)

@router.get("/{attempt_id}/answers", response_model=List[schemas.AttemptAnswerOut])
def get_attempt_answers(attempt_id: int, db: Session = Depends(get_db)):
    return crud.get_attempt_answers(db, attempt_id)