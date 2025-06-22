from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.buy_lists import create_buy_list, get_all, get_all_by_type, get_list_by_id, update_buy_list, delete_buy_list

router = APIRouter()


@router.post("/add_buy_list")
async def add_buy_list(session: AsyncSession = Depends(fastapi_get_db)):
    data = await create_buy_list(session=session)
    return data


@router.get("/")
async def get_all_buy_list(session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_all(session=session)
    return data


@router.get("/type/{list_type}")
async def get_by_type(list_type: str, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_all_by_type(list_type=list_type, session=session)
    return data


@router.get("/{list_id}")
async def get_by_id(list_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    data = await get_list_by_id(list_id=list_id, session=session)
    return data
