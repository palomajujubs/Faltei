from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

import os
import dotenv

#carregar variaveis de ambiente
dotenv.load_dotenv()

db_nome = os.getenv("DB_NOME")
db_user = os.getenv("DB_USER")
db_senha = os.getenv("DB_SENHA")
db_host = os.getenv("DB_HOST")


class Settings(BaseSettings):
    """configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1'
    BD_URL: str = f'postgresql+asyncpg://{db_user}:{db_senha}@{db_host}:5432/{db_nome}'
    DBBaseModel = declarative_base()

    class config:
        case_sensitive =True


settings = Settings()