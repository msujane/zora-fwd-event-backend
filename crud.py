from sqlalchemy.orm import Session
from models import User
from sqlalchemy.exc import IntegrityError

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, name: str, email: str, phone: str = None):
    user = User(name=name, email=email, phone=phone)
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        return None

def update_user_score(db: Session, email: str, score: float):
    user = db.query(User).filter(User.email == email).first()
    if user:
        user.score = score
        db.commit()
        db.refresh(user)
        return user
    return None

def update_user_feedback(db: Session, email: str, feedback: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        user.feedback = feedback
        db.commit()
        db.refresh(user)
        return user
    return None