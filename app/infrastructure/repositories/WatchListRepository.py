from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.dbModels.WatchLists.WatchListEntity import WatchListEntity
from app.models.dbModels.WatchLists.IWatchListRepository import IWatchListRepository


class WatchListRepository(IWatchListRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, watch_list: WatchListEntity) -> WatchListEntity:
        self.session.add(watch_list)
        await self.session.flush()
        return watch_list
    
    async def get_by_id(self, watch_list_id: int) -> Optional[WatchListEntity]:
        query = select(WatchListEntity).where(WatchListEntity.id == watch_list_id)
        result = await self.session.execute(query)
        watch_list = result.scalars().first()
        return watch_list.to_dict() if watch_list else None
    
    async def delete(self, watch_list_id: int) -> bool:
        query = select(WatchListEntity).where(WatchListEntity.id == watch_list_id)
        result = await self.session.execute(query)
        watch_list = result.scalars().first()
        if watch_list:
            self.session.delete(watch_list)
            await self.session.commit()
            return True
        return False
    
    async def get_all(self) -> List[WatchListEntity]:
        query = select(WatchListEntity)
        result = await self.session.execute(query)
        watch_lists = result.scalars().all()
        return [watch_list.to_dict() for watch_list in watch_lists] if watch_lists else []
    
    async def get_all_by_user_id(self, user_id: int) -> List[WatchListEntity]:
        query = select(WatchListEntity).where(WatchListEntity.user_id == user_id)
        result = await self.session.execute(query)
        watch_lists = result.scalars().all()
        return [watch_list.to_dict() for watch_list in watch_lists] if watch_lists else []
