from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.fines import create_fine, get_all_fines, get_fine_by_id

router = APIRouter()


@router.post("/add_fine")
async def add_fine(session: AsyncSession = Depends(fastapi_get_db)):
    data = await create_fine(session=session)
    return data


@router.get("/")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_all_fines(session=session)
    return data


@router.get("/{fine_id}")
async def get_by_id(fine_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_fine_by_id(fine_id=fine_id, session=session)
    return data
