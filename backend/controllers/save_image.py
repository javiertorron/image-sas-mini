from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from PIL import Image
import os

from models.UserModel import UserModel
from services.AuthenticationService import get_current_user

from services.UserMediaService import UserMediaService

router = APIRouter()


# Ruta protegida que procesa la imagen
@router.post("/upload-image")
async def upload_image(user: UserModel = Depends(get_current_user), file: UploadFile = File(...)):
    # Verificar si el archivo es una imagen PNG o JPG
    if not (file.content_type.startswith('image/png') or file.content_type.startswith('image/jpeg')):
        raise HTTPException(status_code=400, detail="Allowed image extensions: PNG, JGP.")

    user_media_service = UserMediaService(user)
    filename = await user_media_service.save_image(await file.read())

    return {"message": "Imagen procesada y guardada en formato webp", "filename": filename}
