# main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware as CORSMiddleware

from controllers import auth, get_file_list, save_image, get_image

app = FastAPI()

app.include_router(auth.router)
app.include_router(get_file_list.router)
app.include_router(get_image.router)
app.include_router(save_image.router)

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:4000",
]

app.add_middleware(

    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)
