from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class RegistrationSchema(BaseModel):
    name: str = Field(..., max_length=255)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)

class ScoreSchema(BaseModel):
    email: EmailStr
    score: float

class FeedbackSchema(BaseModel):
    email: EmailStr
    feedback: str = Field(..., max_length=2000)

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str]
    score: Optional[float]
    feedback: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True