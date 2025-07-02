from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.watch_lists import WatchListService

from app.models.dtoModels.WatchListDTO import WatchListDTO
from app.models.dbModels.WatchLists.WatchListEntity import WatchListEntity as WatchList


router = APIRouter()


@router.post("/add_watch_list")
async def add_watch_list(watch_list: WatchListDTO, session: AsyncSession = Depends(fastapi_get_db)):
    repo = WatchListService(session)

    watch_list_data = WatchList(
        user_id=watch_list.user_id,
        car_id=watch_list.car_id,
        detail_id=watch_list.detail_id
    )
    data = await WatchListService.create(self=repo, watch_list_data=watch_list_data)
    return data

@router.get("/user/{user_id}")
async def get_all_by_user_id(user_id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = WatchListService(session)
    data = await WatchListService.get_all_by_user_id(self=repo, user_id=user_id)
    return data

@router.delete("/delete/{id}")
async def delete(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = WatchListService(session)
    data = await WatchListService.delete(self=repo, watch_list_id=id)
    return data
