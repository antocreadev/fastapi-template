from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import services.user as user
from config import DESCRIPTION, TAGS_METADATA, TITLE
from database import create_database
from routes.auth import router as auth_router
from routes.user import router as user_router

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    openapi_tags=TAGS_METADATA
)

create_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Server"])
async def root():
    return {"message": "API is online, welcome to the API documentation at /docs or /redocs"}

@app.get("/unixTimes", tags=["Server"])
async def read_item():
    unix_timestamp = datetime.now().timestamp()
    return {"unixTime": unix_timestamp}

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])



