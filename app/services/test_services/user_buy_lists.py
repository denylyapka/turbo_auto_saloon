from typing import Any

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.UserBuyListsRepository import UserBuyListsRepository
from app.models.dbModels.UserBuyLists.UserBuyListsEntity import UserBuyListsEntity as UserBuyList


class UserBuyListsService:
    def __init__(self, session: AsyncSession):
        self.repo = UserBuyListsRepository(session)
        self.session = session
    
    async def create(self, user_buy_list: UserBuyList) -> UserBuyList:
        return await self.repo.create(user_buy_list)
    
    async def update(self, user_buy_list: UserBuyList) -> UserBuyList:
        return await self.repo.update(user_buy_list)
    
    async def delete(self, user_buy_list_id: int) -> bool:
        return await self.repo.delete(user_buy_list_id)
    
    async def delete_by_user_and_list(self, user_id: int, buy_list_id: int) -> bool:
        return await self.repo.delete_by_user_and_list(user_id, buy_list_id)
    
    async def get_by_user_id(self, user_id: int) -> Any:
        return await self.repo.get_by_user_id(user_id)
    
    async def get_by_buy_list_id(self, buy_list_id: int) -> Any:
        return await self.repo.get_by_buy_list_id(buy_list_id)
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, user_buy_list_id: int) -> Any:
        return await self.repo.get_by_id(user_buy_list_id)

