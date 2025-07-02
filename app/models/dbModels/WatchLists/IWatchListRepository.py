from typing import Optional
from app.models.dbModels.WatchLists.WatchListEntity import WatchListEntity

class IWatchListRepository:
    async def create(self, watch_list: WatchListEntity) -> WatchListEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, watch_list_id: int) -> Optional[WatchListEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, watch_list_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> list[WatchListEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_user_id(self, user_id: int) -> list[WatchListEntity]:
        raise NotImplementedError("Метод не реализован!")
