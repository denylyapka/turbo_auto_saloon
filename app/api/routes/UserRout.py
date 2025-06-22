from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.user import create_user, get_user_by_id

router = APIRouter()



@router.get("/test")
async def test():
    return {"test": "test"}


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_user_by_id(user_id=id, session=session)
    return data


@router.post("/add_user")
async def add_user(session: AsyncSession = Depends(fastapi_get_db)):
    data = await create_user(session=session)
    return data
