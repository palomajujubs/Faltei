from core.configs import settings

from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'

    codigo: str = Column(String, primary_key= True,
                          autoincrement= False, 
                          unique=True, 
                          nullable=False)
    titulo: str = Column(String(100), nullable=False)
    dias: str = Column(String (100), nullable=False)
    horas: int = Column(Integer, nullable=False)
    faltas: int = Column(Integer,nullable=False)

