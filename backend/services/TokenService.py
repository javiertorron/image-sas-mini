# Configuración de autenticación
from datetime import datetime, timedelta
from jose import JWTError, jwt

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
    except ExpiredTokenException:
        return None
    except UnauthorizedException:
        return None
    except JWTError:
        return None
