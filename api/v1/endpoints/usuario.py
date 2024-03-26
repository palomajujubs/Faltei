from fastapi import APIRouter, status, Depends

from fastapi.responses import JSONResponse


from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select



router = APIRouter()


@router.post('/')
...