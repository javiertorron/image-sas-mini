# main.py

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from controllers import auth, user
from services.AuthenticationService import authenticate
from services.TokenService import get_access_token_expiration, create_access_token

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)

# Configuración de autenticación
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Ruta para obtener token de acceso
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
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


# Ruta protegida que requiere autenticación
@app.get("/images")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return fake_users_db[token]
