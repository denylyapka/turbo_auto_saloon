from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.buy_lists import BuyListService


router = APIRouter()


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.get_by_id(self=repo, list_id=id)
    return data

@router.get("/")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.get_all(self=repo)
    return data

@router.get("/type/{list_type}")
async def get_by_type(list_type: str, session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.get_all_by_type(self=repo, list_type=list_type)
    return data

@router.post("/add_buy_list")
async def add_buy_list(session: AsyncSession = Depends(fastapi_get_db)):
    repo = BuyListService(session)
    data = await BuyListService.create(self=repo)
    return data

