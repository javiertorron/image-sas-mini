# Mock de usuarios
from fastapi import Depends
from passlib.context import CryptContext

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
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = fake_users_db.get(username)
    if not user:
        return False
    if not pwd_context.verify(password, user["hashed_password"]):
        return False
    return user


async def get_current_user(user: str = Depends(decode_access_token)):
    if not user:
        raise UnauthorizedException(detail="Unauthorized token")
    return user
