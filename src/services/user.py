from typing import Annotated, Optional

from fastapi import Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

import src.tasks as tasks
from src.models.user import User
from src.schemas.user import UserCreate, UserResponse
from src.services.file import upload_file


async def get_all_users(db: Session) -> list[UserResponse] :
    return db.query(User).all()

async def add_user(
    db: Session, 
    user: UserCreate, 
    img: Optional[UploadFile] = None,
    mime_type: Optional[str] = None
) -> User:
    hashed_password = tasks.get_password_hash(user.password)
    
    img_file = None
    if img:
        img_file = upload_file(
            file_content=img.file,
            filename=img.filename,
            content_type=mime_type
        )
    
    db_user = User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        img=img_file,
        password=hashed_password,
        rgpd=user.rgpd,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Convertir l'objet File en dictionnaire si présent
    if db_user.img:
        db_user.img = dict(db_user.img)
    
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
