# Mock de usuarios
from fastapi import Depends
import bcrypt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from exceptions.UnauthorizedException import UnauthorizedException
from mocks.DbMock import fake_users_db
from services.TokenService import decode_access_token

bearer_scheme = HTTPBearer()


def authenticate(username: str, password: str):
    """
    Recibe usuario y contraseña para autenticar contra nuestro mock

    :param username:
    :param password:
    :return:
    """
    user = fake_users_db.get(username)
    print(f"Inicial: {password}")
    password_check = check_password(password, user["hashed_password"])

    if not user:
        return False
    if not password_check:
        return False
    return user


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    user = decode_access_token(credentials.credentials)
    return user if user else None


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    print(f"Verificando contraseña:")
    print(f"Recibimos {plain_text_password} y verificamos contra {hashed_password}")
    return bcrypt.checkpw(plain_text_password.encode(), hashed_password.encode())
