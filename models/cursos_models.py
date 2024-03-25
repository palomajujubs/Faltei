from core.configs import settings

from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'

    codigo: str = Column(String, primary_key= True, autoincrement= False)
    titulo: str = Column(String(100))
    dias: str = Column(String (100))
    horas: int = Column(Integer)
    faltas: int = Column(Integer)

