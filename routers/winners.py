from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from .. import crud, schemas

router = APIRouter(
    prefix="/winners",
    tags=["winners"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/latest", response_model=List[schemas.WinnerOut])
def get_latest_winners(count: int = 3, db: Session = Depends(get_db)):
    return crud.get_latest_winners(db, count)