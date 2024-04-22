# main.py

from fastapi import FastAPI

from controllers import auth, get_file_list, save_image, get_image

app = FastAPI()

app.include_router(auth.router)
app.include_router(get_file_list.router)
app.include_router(get_image.router)
app.include_router(save_image.router)
