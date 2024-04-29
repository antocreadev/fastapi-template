
# --- Importation des modules
# pydantic est utilisé pour la validation des données
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

# --- Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str = None

# --- User schemas
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    rgpd: bool
    following: List["User"] = []
    
# UserCreate est utilisé pour la création d'un utilisateur, il contient un champ password + les champs de UserBase
class UserCreate(UserBase):
    password: str

# User est utilisé pour la lecture d'un utilisateur, il contient un champ id + les champs de UserBase
class User(UserBase):
    id: int
    class Config:
        from_attributes = True

