from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    codigo: str
    titulo: str
    dias: str
    horas: int
    faltas: int

    class config: 
        orm_mode = True