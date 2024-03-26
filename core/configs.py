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

jwt_token = os.getenv("JWT_SECRET")

class Settings(BaseSettings):
    """configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1'
    BD_URL: str = f'postgresql+asyncpg://{db_user}:{db_senha}@{db_host}:5432/{db_nome}'
    DBBaseModel: DeclarativeMeta = declarative_base()

    JWT_SECRET: str = f'{jwt_token}'
    ALGORITHM: str = 'HS256'
#tempo de acesso do token em uma semana
    ACCESS_TOKEN_EXPIRE_MINUTES: 60 * 24 * 7 # type: ignore


    class config:
        case_sensitive =True


settings = Settings()