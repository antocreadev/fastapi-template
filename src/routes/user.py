import imghdr
from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

import src.dependencies as dependencies
import src.services.user as user
from src.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/get/all/", response_model=list[UserResponse], tags=["Users"])
async def read_users(
    current_user: Annotated[UserResponse, Depends(dependencies.get_current_user)],
    db: Session = Depends(dependencies.get_db)
)-> list[UserResponse]:
    return await user.get_all_users(db)

@router.post("/add/", response_model=UserResponse, tags=["Users"])
async def add_user(
    firstname: str = Form(...),
    lastname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    rgpd: bool = Form(...),
    img: UploadFile = File(None),
    db: Session = Depends(dependencies.get_db)
)-> UserResponse:
    detected_mime_type = None
    if img:
        # Lire le contenu de l'image
        contents = await img.read()
        # Détecter le type d'image
        img_format = imghdr.what(None, contents)
        
        if img_format not in ['png', 'jpeg', 'gif']:
            raise HTTPException(
                status_code=400,
                detail="Le fichier doit être une image (PNG, JPEG ou GIF)"
            )
        
        # Définir le bon type MIME
        mime_types = {
            'png': 'image/png',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif'
        }
        
        # Réinitialiser le curseur du fichier pour la lecture ultérieure
        await img.seek(0)
        detected_mime_type = mime_types[img_format]

    user_data = UserCreate(
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password,
        rgpd=rgpd
    )
    
    return await user.add_user(db, user_data, img, detected_mime_type)

@router.get("/me/", response_model=UserResponse, tags=["Users"])
async def read_users_me(
    current_user: Annotated[UserResponse, Depends(dependencies.get_current_user)]
):
    return current_user
