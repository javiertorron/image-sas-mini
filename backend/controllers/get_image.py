import os

from fastapi import APIRouter, Depends, HTTPException
from models.UserModel import UserModel
from fastapi.responses import FileResponse
from services.UserMediaService import UserMediaService
from services.AuthenticationService import get_current_user

router = APIRouter()


@router.get("/get-image/{filename}")
async def get_image(filename: str, user: UserModel = Depends(get_current_user)):
    user_media_service = UserMediaService(user)
    image_path = user_media_service.get_image_path(filename)
    if image_path:
        return FileResponse(image_path, media_type="image/webp")
    else:
        raise HTTPException(status_code=404, detail="La imagen no existe")
