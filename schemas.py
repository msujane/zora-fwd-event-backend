
from pydantic import BaseModel, field_validator,EmailStr
from typing import Optional, Dict, List
import re

class UserCreate(BaseModel):


    name: str
    email: str
    phone: Optional[str] = None

    @field_validator('email')
    def must_be_deloitte_email(cls, v):
        if not v.lower().endswith('@deloitte.com'):
            raise ValueError("Email must be a @deloitte.com address")
        return v
    

    @field_validator('phone')
    def valid_phone_number(cls, v):
        if v:
            # Accepting only 10 digit numbers, adjust as needed for your locale
            if not re.fullmatch(r'\d{10}', v):
                raise ValueError("Phone must be a 10-digit number")
        return v


class MiniUser(BaseModel):
    name: str
    email: EmailStr
    score: int
    time_taken: int
    passed: bool

    class Config:
        orm_mode = True

class AdminPollResult(BaseModel):
    names: List[str]
    scores: List[int]

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    score: int
    time_taken: int
    class Config:
        orm_mode = True

class QuestionOut(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    class Config:
        orm_mode = True

class AttemptSubmission(BaseModel):
    email: str
    answers: Dict[int, str]  # {question_id: option ("a"/"b"/"c"/"d")}
    time_taken: int  # time in seconds

class FeedbackCreate(BaseModel):
    email: str
    point1: str
    point2: str
    point3: str
    point4: Optional[str] = None

class FeedbackOut(BaseModel):
    id: int
    user_email: str
    point1: str
    point2: str
    point3: str
    point4: Optional[str] = None
    class Config:
        orm_mode = True

class WinnerOut(BaseModel):
    name: str
    email: str
    score: int
    time_taken: int
    class Config:
        orm_mode = True

