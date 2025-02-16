import uuid
from datetime import datetime
from typing import Literal, Optional, Union

from pydantic import EmailStr, BaseModel


class ItemRead(BaseModel):
    id : int
    name: str
    created_at: datetime
    owner_id: str

class ItemCreate(BaseModel):
    name: str

class ItemUpdate(BaseModel):
    name: Optional[str]