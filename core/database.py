from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.BD_URL)

Session: AsyncSession = sessionmaker(
    autommit=False,
    autoflush=False,
    expire_on_commit= False,
    class_= AsyncSession,
    bind= engine 

)