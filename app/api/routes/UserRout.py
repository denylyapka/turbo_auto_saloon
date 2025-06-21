from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.testservices import test_service, get_user_by_id

router = APIRouter()



@router.get("/test")
async def test():
    return {"test": "test"}


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_user_by_id(user_id=id, session=session)
    return data


@router.post("/create_user")
async def create_user(session: AsyncSession = Depends(fastapi_get_db)):
    data = await test_service(session=session)
    return data
