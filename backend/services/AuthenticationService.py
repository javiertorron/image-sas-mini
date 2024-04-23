# Mock de usuarios
from fastapi import Depends
from passlib.context import CryptContext
import bcrypt
from exceptions.UnauthorizedException import UnauthorizedException
from mocks.DbMock import fake_users_db
from services.TokenService import decode_access_token


def authenticate(username: str, password: str):
    """
    Recibe usuario y contraseña para autenticar contra nuestro mock

    :param username:
    :param password:
    :return:
    """
    user = fake_users_db.get(username)
    password_check = check_password(password, user["hashed_password"])
    if not user:
        return False
    if not password_check:
        return False
    return user


async def get_current_user(user: str = Depends(decode_access_token)):
    if not user:
        raise UnauthorizedException(detail="Unauthorized token")
    return user


def check_password(password: str, hashed_password: str) -> bool:
    # Convertir la contraseña y el hash almacenado a bytes.
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    print(f"Password: {password_bytes}")
    print(f"Hash Password: {hashed_password_bytes}")
    # Verificar la contraseña con el hash almacenado.
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)