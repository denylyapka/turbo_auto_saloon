import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.BuyListsRepository import BuyListsRepository
from app.models.dbModels.BuyLists.BuyListsEntity import BuyListsEntity as BuyList


class BuyListService:
    def __init__(self, session: AsyncSession):
        self.repo = BuyListsRepository(session)
        self.session = session

    async def get_by_id(self, list_id: int) -> BuyList:
        return await self.repo.get_by_id(list_id=list_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def get_all_by_type(self, list_type: str) -> Any:
        return await self.repo.get_by_type(list_type=list_type)

    async def create(self, list_type: str = "type", 
                    products: str = "products", 
                    total_price: int = 123456, 
                    total_discount: int = 10) -> BuyList:
        buy_list = BuyList(
            type=list_type,
            products=products,
            datetime_create=datetime.datetime.now(),
            total_price=total_price,
            total_discount=total_discount
        )
        return await self.repo.create(buy_list=buy_list)

    async def update(self, buy_list: BuyList) -> BuyList:
        return await self.repo.update(buy_list=buy_list)

    async def delete(self, list_id: int) -> bool:
        return await self.repo.delete(list_id=list_id)