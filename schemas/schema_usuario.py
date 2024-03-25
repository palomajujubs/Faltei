from typing import Optional
from pydantic import BaseModel as SCBaseModel

class UsuarioSchema(SCBaseModel):
    email: str
    nome: str
    universidade: str

    class config: 
        orm_mode = True