
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    rgpd: bool
    following: List["UserResponse"] = []
    
class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True

