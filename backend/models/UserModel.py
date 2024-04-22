from pydantic import BaseModel


# Modelos Pydantic para usuarios
class UserModel(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = None
    id: str
