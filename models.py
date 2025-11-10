

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, nullable=True)
    score = Column(Integer, default=0)
    time_taken = Column(Integer, default=0)  # seconds for tie-breaker
    has_attempted = Column(Boolean, default=False)  # NEW: track quiz attempt
    is_admin = Column(Boolean, default=False)  # <-- NEW FIELD to  check is  admin or  not



class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_option = Column(String, nullable=False)  # One of: "a","b","c","d"



    correct_option = Column(String, nullable=False)  # One of: "a","b","c","d"

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, ForeignKey("users.email"))
    point1 = Column(String)
    point2 = Column(String)
    point3 = Column(String)
    point4 = Column(String, nullable=True)
    user = relationship("User")