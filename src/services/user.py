from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

import tasks as tasks
from models.user import User
from schemas.user import UserCreate, UserResponse


async def get_all_users(db: Session) -> list[UserResponse] :
    return db.query(User).all()

async def add_user(db: Session, user: UserCreate) -> User:
    hashed_password = tasks.get_password_hash(user.password)
    db_user = User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=hashed_password,
        rgpd=user.rgpd,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not tasks.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = tasks.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
