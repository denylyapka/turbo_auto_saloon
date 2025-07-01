from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.dbModels.WatchLists.WatchListEntity import WatchListEntity
from app.models.dbModels.WatchLists.IWatchListRepository import IWatchListRepository


class WatchListRepository(IWatchListRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, discount: WatchListEntity) -> WatchListEntity:
        self.session.add(discount)
        await self.session.flush()
        return discount
    
    async def get_by_id(self, discount_id: int) -> Optional[WatchListEntity]:
        query = select(WatchListEntity).where(WatchListEntity.id == discount_id)
        result = await self.session.execute(query)
        discount = result.scalars().first()
        return discount.to_dict()
    
    async def delete(self, discount_id: int) -> bool:
        query = select(WatchListEntity).where(WatchListEntity.id == discount_id)
        result = await self.session.execute(query)
        discount = result.scalars().first()
        if discount:
            self.session.delete(discount)
            await self.session.commit()
            return True
        return False
    
    async def get_all(self) -> List[WatchListEntity]:
        query = select(WatchListEntity)
        result = await self.session.execute(query)
        discounts = result.scalars().all()
        return [discount.to_dict() for discount in discounts] if discounts else []
    
    async def get_all_by_user_id(self, user_id: int) -> List[WatchListEntity]:
        query = select(WatchListEntity).where(WatchListEntity.user_id == user_id)
        result = await self.session.execute(query)
        discounts = result.scalars().all()
        return [discount.to_dict() for discount in discounts] if discounts else []
