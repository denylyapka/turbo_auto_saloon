from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import fastapi_get_db
from app.services.test_services.watch_lists import WatchListService


router = APIRouter()


@router.get("/")
async def get_all(session: AsyncSession = Depends(fastapi_get_db)):
    repo = WatchListService(session)
    data = await WatchListService.get_all(self=repo)
    return data

@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(fastapi_get_db)):
    repo = WatchListService(session)
    data = await WatchListService.get_by_id(self=repo, watch_list_id=id)
    return data