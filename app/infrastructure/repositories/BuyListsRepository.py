from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from datetime import datetime
from app.models.dbModels.BuyLists.BuyListsEntity import BuyListsEntity
from app.models.dbModels.BuyLists.IBuyListsRepository import IBuyListsRepository

class BuyListsRepository(IBuyListsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, buy_list: BuyListsEntity) -> BuyListsEntity:
        self.session.add(buy_list)
        await self.session.commit()
        await self.session.refresh(buy_list)
        return buy_list

    async def get_by_id(self, list_id: int) -> Optional[BuyListsEntity]:
        query = select(BuyListsEntity).where(BuyListsEntity.id == list_id)
        result = await self.session.execute(query)
        buy_list = result.scalars().first()
        return buy_list.to_dict() if buy_list else None

    async def get_by_type(self, list_type: str) -> List[BuyListsEntity]:
        query = select(BuyListsEntity).where(BuyListsEntity.type == list_type)
        result = await self.session.execute(query)
        buy_lists = result.scalars().all()
        return [buy_list.to_dict() for buy_list in buy_lists]

    async def get_all(self) -> List[BuyListsEntity]:
        query = select(BuyListsEntity)
        result = await self.session.execute(query)
        buy_lists = result.scalars().all()
        return [buy_list.to_dict() for buy_list in buy_lists]

    async def update(self, buy_list: BuyListsEntity) -> BuyListsEntity:
        await self.session.commit()
        await self.session.refresh(buy_list)
        return buy_list

    async def delete(self, list_id: int) -> bool:
        buy_list = await self.get_by_id(list_id)
        if buy_list:
            await self.session.delete(buy_list)
            await self.session.commit()
            return True
        return False

    async def search(
        self,
        list_type: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None
    ) -> List[BuyListsEntity]:
        query = select(BuyListsEntity)

        filters = {
            'type': (BuyListsEntity.type.ilike, f"%{list_type}%"),
            'min_price': (BuyListsEntity.total_price >= min_price),
            'max_price': (BuyListsEntity.total_price <= max_price),
            'date_from': (BuyListsEntity.datetime_create >= date_from),
            'date_to': (BuyListsEntity.datetime_create <= date_to)
        }

        for param, (condition, value) in filters.items():
            if value is not None:
                query = query.where(condition(value))

        result = await self.session.execute(query)
        buy_lists = result.scalars().all()
        return [buy_list.to_dict() for buy_list in buy_lists]
