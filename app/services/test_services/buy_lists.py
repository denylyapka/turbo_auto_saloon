from typing import Any

from fastapi import HTTPException
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
    
    async def get_products_by_buy_list_id(self, buy_list_id: int) -> Any:
        return await self.repo.get_products_by_buy_list_id(buy_list_id=buy_list_id)

    async def create(self, buy_list: BuyList) -> dict:
        return await self.repo.create(buy_list=buy_list)

    async def update(self, buy_list_entity: BuyList) -> dict:
        # Проверяем существование записи
        existing = await self.repo.get_by_id(buy_list_entity.id)
        if not existing:
            raise HTTPException(status_code=404, detail="Buy list not found")
            
        return await self.repo.update(buy_list=buy_list_entity)

    async def delete(self, list_id: int) -> bool:
        return await self.repo.delete(list_id=list_id)
    
    async def delete_product(self, buy_list_id: int, product_index: int) -> bool:
        return await self.repo.delete_product(buy_list_id=buy_list_id, product_index=product_index)
    
