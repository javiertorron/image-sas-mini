# Configuración de autenticación
from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import JWTError, jwt
import bcrypt
from pydantic import ValidationError

from exceptions.ExpiredTokenException import ExpiredTokenException
from exceptions.UnauthorizedException import UnauthorizedException
from mocks.DbMock import fake_users_db
from models.TokenData import TokenData
from models.UserModel import UserModel

SECRET_KEY = 'CU/Fo/~H|"jai|VmXM9:}1OIjK2,XU+0@Y.x$e%3:H)K"tWq9H!}Qzy82`7="Co'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def get_access_token_expiration():
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


# Funciones para generar y verificar tokens
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        print(f"--------------> Token: {token}")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Verificamos si el token ha expirado
        expiration_timestamp = payload.get("exp")
        if expiration_timestamp is None or datetime.utcfromtimestamp(expiration_timestamp) < datetime.utcnow():
            raise ExpiredTokenException()
        username: str = payload.get("sub")
        if username is None:
            return None
        user_data = fake_users_db.get(username)
        return UserModel(**user_data)
    except ExpiredTokenException as exp:
        print(f"Expired token exception: {exp}")
        return None
    except UnauthorizedException:
        print("Unsauthorized exception")
        return None
    except JWTError as jwtExp:
        print(f"JWT error: {jwtExp}")
        return None
    except ValidationError as val:
        print(f"ValidationError: {val}")
        raise HTTPException(status_code=400, detail=f"Invalid data: {val.errors()}")


def encrypt_password(password: str) -> str:
    password_bytes = password.encode('utf-8')

    # Generar el salt y hashear la contraseña.
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # Devolver la contraseña hasheada en formato de cadena para almacenar en la base de datos.
    return hashed_password.decode('utf-8')
