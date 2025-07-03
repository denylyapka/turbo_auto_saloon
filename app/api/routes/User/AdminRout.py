from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db

from app.services.test_services.user import get_all


router = APIRouter()


@router.get("/")
async def get_all_users(session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_all(session=session)
    return data