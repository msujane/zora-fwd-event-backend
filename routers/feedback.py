from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from .. import crud, schemas

router = APIRouter(
    prefix="/feedback",
    tags=["feedback"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.FeedbackOut)
def submit_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db, feedback)