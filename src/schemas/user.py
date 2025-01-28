from typing import List, Optional

from fastapi import UploadFile
from pydantic import BaseModel


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    rgpd: bool


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    img: Optional[dict] = None

    class Config:
        from_attributes = True

