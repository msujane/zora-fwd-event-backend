# Authors : Ajinkya A, Subshree S

from fastapi import FastAPI, Depends, HTTPException,Query
from sqlalchemy.orm import Session
import crud, schemas, models
from database import engine, get_db,Base
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/user/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

@app.get("/api/user/questions", response_model=List[schemas.QuestionOut])
def get_questions(db: Session = Depends(get_db)):
    questions = crud.get_random_questions(db, 5)
    return questions


# from database import engine, Base  # adjust imports if needed
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
@app.post("/api/user/submit", response_model=schemas.UserOut)
def submit_attempt(attempt: schemas.AttemptSubmission, db: Session = Depends(get_db)):
    user,error = crud.submit_attempt(db, attempt.email, attempt.answers, attempt.time_taken)
    if user:
        return user
    else:
        if error == "User not found":
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)
# @app.post("/api/user/feedback", response_model=schemas.FeedbackOut)
# def feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
#     return crud.submit_feedback(db, feedback)

# @app.get("/api/winners", response_model=List[schemas.WinnerOut])
# def winners(db: Session = Depends(get_db)):
#     return crud.get_winners(db)



@app.get("/api/admin/users", response_model=List[schemas.MiniUser])
def admin_get_all_users(
    admin_email: str = Query(...), db: Session = Depends(get_db)
):
    if not crud.is_admin(db, admin_email):
        raise HTTPException(status_code=403, detail="Not authorized as admin")
    users = crud.get_all_users(db)
    mini_users = [
        schemas.MiniUser(
            name=u.name,
            email=u.email,
            score=u.score,
            time_taken=u.time_taken,
            passed=u.score >= 12    # Use your threshold
        ) for u in users
    ]
    return mini_users

@app.get("/api/admin/poll_top3", response_model=schemas.AdminPollResult)
def admin_poll_top_three(
    admin_email: str = Query(...), db: Session = Depends(get_db)
):
    if not crud.is_admin(db, admin_email):
        raise HTTPException(status_code=403, detail="Not authorized as admin")
    top_users = crud.get_top_n_users(db, 3)
    return schemas.AdminPollResult(
        names=[u.name for u in top_users],
        scores=[u.score for u in top_users]
    )