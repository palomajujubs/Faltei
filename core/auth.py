from pytz import timezone

from typing import Optional, List
from datetime  import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from jose import jwt

from models.usuario_model import UsuarioModel
from core.configs import settings
from core.security import verificar_senha


from pydantic import EmailStr

oauth_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)

async def autenticer(email: EmailStr, senha:str, db: AsyncSession)-> Optional(UsuarioModel):
    async with db as session:
        query= select(UsuarioModel).filter(UsuarioModel.email == email)
        result=  await session.execute(query)
        usuario: UsuarioModel= result.scalar().unique().one_or_none()

        if not usuario:
            return None
        if not verificar_senha(senha, usuario.senha):
            return None


def criar_token(tipo_token: str,
                tempo_vida: timedelta,
                sub: str) ->str:
    payload = {}

    ba = timezone('America/Bahia')
    expira = datetime.now(tz=ba) + tempo_vida

    payload["type"] = tipo_token

    payload["exp"] = expira

    payload["iat"] = datetime.now(tz=ba)

    payload["sub"] = str(sub) 

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def criar_token_acesso( sub:str) ->str:
    return criar_token(
        tipo_token= 'acess_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub= sub
    )