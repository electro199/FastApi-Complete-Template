import uuid
from datetime import datetime
from typing import Literal, Optional, Union

from pydantic import EmailStr, BaseModel


class UserRead(BaseModel):
    name: str
    email: EmailStr
    profile_picture: Optional[str] = None
    created_at: datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[str] = None
