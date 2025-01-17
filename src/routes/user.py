from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import dependencies
import services.user as user
from schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/get/all/", response_model=list[UserResponse], tags=["Users"])
async def read_users(
    current_user: Annotated[UserResponse, Depends(dependencies.get_current_user)],
    db: Session = Depends(dependencies.get_db)
)-> list[UserResponse]:
    return await user.get_all_users(db)

@router.post("/add/", response_model=UserResponse, tags=["Users"])
async def add_user(
    user_create: UserCreate,
    db: Session = Depends(dependencies.get_db)
)-> UserResponse:
    return await user.add_user(db, user_create)

@router.get("/me/", response_model=UserResponse, tags=["Users"])
async def read_users_me(
    current_user: Annotated[UserResponse, Depends(dependencies.get_current_user)]
):
    return current_user
