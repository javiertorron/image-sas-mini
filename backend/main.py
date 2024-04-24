# main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware as CORSMiddleware

from controllers import auth, get_image_list, save_image, get_image
from middleware.custom_cors_middleware import CustomCORSMiddleware

app = FastAPI()

app.include_router(auth.router)
app.include_router(get_image_list.router)
app.include_router(get_image.router)
app.include_router(save_image.router)

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:4000",
]

app.add_middleware(
    CustomCORSMiddleware
)
