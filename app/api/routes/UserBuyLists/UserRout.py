from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.user_buy_lists import UserBuyListsService

from app.models.dtoModels.UserBuyListsDTO import UserBuyListsDTO

from app.models.dbModels.UserBuyLists.UserBuyListsEntity import UserBuyListsEntity


router = APIRouter()


@router.get("/")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    service = UserBuyListsService(session)
    data = await service.get_all()
    return data

@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    service = UserBuyListsService(session)
    data = await service.get_by_id(user_buy_list_id=id)
    return data

@router.get("/user/{user_id}")
async def get_by_user_id(user_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    service = UserBuyListsService(session)
    data = await service.get_by_user_id(user_id=user_id)
    return data

@router.get("/list/{buy_list_id}")
async def get_by_buy_list_id(buy_list_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    service = UserBuyListsService(session)
    data = await service.get_by_buy_list_id(buy_list_id=buy_list_id)
    return data

@router.delete("/{id}")
async def delete(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    service = UserBuyListsService(session)
    data = await service.delete(user_buy_list_id=id)
    return data
