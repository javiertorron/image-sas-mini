import os
from PIL import Image
import uuid
from models.UserModel import UserModel


class UserMediaService:
    def __init__(self, user: UserModel):
        self.user = user

    def save_image(self, file: bytes) -> bool:
        try:
            # Crear directorio para el usuario si no existe
            user_media_dir = f"mocks/media/{self.user.id}"
            os.makedirs(user_media_dir, exist_ok=True)

            # Guardar la imagen en formato webp
            original_image = Image.open(file)
            new_filename = str(uuid.uuid4())

            # Guardamos la foto en tamaño web
            resized_image = original_image.copy()
            resized_image.thumbnail((1080, 920))
            resized_path = f"{user_media_dir}/{new_filename}.webp"
            resized_image.save(resized_path, "WEBP")

            # Guardamos una miniatura para las listas
            thumbnail_image = original_image.copy()
            thumbnail_image.thumbnail((100, 100))
            thumbnail_path = f"{user_media_dir}/thumbnail_{new_filename}.webp"
            thumbnail_image.save(thumbnail_path, "WEBP")

            return True
        except Exception as e:
            # Si no puede guardar la imagen devolvemos False
            return False

    def get_image_path(self, filename: str):
        # Obtener la ruta de la imagen webp
        user_media_dir = f"mocks/media/{self.user.id}"
        webp_path = f"{user_media_dir}/{filename}"

        # Verificar si la imagen existe
        if os.path.exists(webp_path):
            return webp_path
        else:
            return None

    def get_user_images(self):
        # Obtener la ruta del directorio del usuario
        user_media_dir = f"mocks/media/{self.user.id}"

        # Verificar si el directorio del usuario existe
        if not os.path.exists(user_media_dir):
            return []

        # Obtener la lista de archivos en el directorio del usuario
        user_files = os.listdir(user_media_dir)

        # Filtrar solo los archivos con extensión ".webp" y cuyo nombre comience por "thumbnail_"
        thumbnail_files = [file for file in user_files if file.endswith(".webp") and file.startswith("thumbnail_")]

        return thumbnail_files
