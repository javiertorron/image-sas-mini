# auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dtos.LoginRequestDTO import LoginRequestDTO
from services.AuthenticationService import authenticate
from services.TokenService import get_access_token_expiration, create_access_token, encrypt_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


@router.post("/token")
async def login_for_access_token(form_data: LoginRequestDTO):
    user = authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = get_access_token_expiration()
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    # Retorna el token de acceso y el refresh token si la autenticación es exitosa
    return {"access_token": access_token, "token_type": "bearer"}
