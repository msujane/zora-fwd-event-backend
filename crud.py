
from sqlalchemy.orm import Session
import models , schemas
import random
from models import User

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def is_admin(db, email: str):
    user = db.query(models.User).filter(models.User.email == email, models.User.is_admin == 1).first()
    return bool(user)

def get_all_users(db):
    return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_top_n_users(db, n=3):
    return db.query(models.User).filter(models.User.has_attempted == True).order_by(models.User.score.desc(), models.User.time_taken).limit(n).all()


def get_random_questions(db: Session, n: int = 5):
    all_qs = db.query(models.Question).all()
    return random.sample(all_qs, min(n, len(all_qs)))



def submit_attempt(db: Session, email: str, answers: dict, time_taken: int):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return None, "User not found"
    if user.has_attempted:
        return None, "User has already attempted the quiz"

    score = 0
    for qid, selected in answers.items():
        q = db.query(models.Question).filter(models.Question.id == int(qid)).first()
        if q and q.correct_option.lower() == selected.lower():
            score += 1
    user.score = score
    user.time_taken = time_taken
    user.has_attempted = True  # Block further attempts!
    db.commit()
    db.refresh(user)
    return user, None

def submit_feedback(db: Session, feedback: schemas.FeedbackCreate):
    db_feedback = models.Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

# def get_winners(db: Session, top_n: int = 3):
#     users = db.query(models.User).order_by(
#         models.User.score.desc(), models.User.time_taken
#     ).limit(top_n).all()
#     return users


def get_top3_users(db: Session):
    # Only users who have attempted the quiz (not admins)
    users = db.query(User).filter(
        User.has_attempted == True,
        User.is_admin == False
    ).order_by(User.score.desc(), User.time_taken.asc()).all()
    if len(users) < 3:
        return None  # Or you could raise a custom exception
    return users[:3]