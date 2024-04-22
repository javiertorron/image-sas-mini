from fastapi import APIRouter, Depends
from models import UserModel
from services.UserMediaService import UserMediaService
from services.AuthenticationService import get_current_user

router = APIRouter()


# Ruta protegida que devuelve la lista de imágenes de un usuario
@router.get("/file-list")
async def get_file_list(user: UserModel = Depends(get_current_user)):
    # Obtener la lista de imágenes del usuario
    user_media_service = UserMediaService(user)

    return {
        "files": user_media_service.get_user_images()
    }