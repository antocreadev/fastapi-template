from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas.token import Token
from services.user import authenticate_user

router = APIRouter()

@router.post("/token/",response_model=Token, tags=["Auth"])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
)-> Token:
    return await authenticate_user(db, form_data.username, form_data.password)