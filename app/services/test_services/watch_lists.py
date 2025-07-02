import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.WatchListRepository import WatchListRepository
from app.models.dbModels.WatchLists.WatchListEntity import WatchListEntity as WatchList


class WatchListService:
    def __init__(self, session: AsyncSession):
        self.repo = WatchListRepository(session)    
        self.session = session

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def get_all_by_user_id(self, user_id: int) -> Any:
        return await self.repo.get_all_by_user_id(user_id)

    async def delete(self, watch_list_id: int) -> Any:
        return await self.repo.delete(watch_list_id)

    async def create(self, watch_list_data: WatchList) -> Any:
        return await self.repo.create(watch_list_data)

    async def get_by_id(self, watch_list_id: int) -> Any:
        return await self.repo.get_by_id(watch_list_id)
