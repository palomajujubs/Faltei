from core.configs import settings

from sqlalchemy import Column, String, Integer
 

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    email: str = Column(String(256),
                        index=True,
                        primary_key= True,
                        unique=True,
                        nullable=False)
    nome: str = Column(String (255))
    Universidade: str= Column(String(255))
    senha: str = Column(String(255), nullable=False)