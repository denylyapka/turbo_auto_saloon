from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.dbModels.UserBuyLists.UserBuyListsEntity import UserBuyListsEntity
from app.models.dbModels.UserBuyLists.IUserBuyListsRepository import IUserBuyListsRepository

class UserBuyListsRepository(IUserBuyListsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_buy_list: UserBuyListsEntity) -> UserBuyListsEntity:
        self.session.add(user_buy_list)
        await self.session.commit()
        await self.session.refresh(user_buy_list)
        return user_buy_list

    async def get_by_id(self, user_buy_list_id: int) -> Optional[UserBuyListsEntity]:
        query = select(UserBuyListsEntity).where(UserBuyListsEntity.id == user_buy_list_id)
        result = await self.session.execute(query)
        return result.scalars().first().to_dict()

    async def get_by_user_id(self, user_id: int) -> List[UserBuyListsEntity]:
        query = select(UserBuyListsEntity).where(UserBuyListsEntity.user_id == user_id)
        result = await self.session.execute(query)
        user_bls = result.scalars().all()
        return [user_bl.to_dict() for user_bl in user_bls]

    async def get_by_buy_list_id(self, buy_list_id: int) -> List[UserBuyListsEntity]:
        query = select(UserBuyListsEntity).where(UserBuyListsEntity.buy_list_id == buy_list_id)
        result = await self.session.execute(query)
        user_bls = result.scalars().all()
        return [user_bl.to_dict() for user_bl in user_bls]

    async def get_all(self) -> List[UserBuyListsEntity]:
        query = select(UserBuyListsEntity)
        result = await self.session.execute(query)
        user_bls = result.scalars().all()
        return [user_bl.to_dict() for user_bl in user_bls]

    async def update(self, user_buy_list: UserBuyListsEntity) -> UserBuyListsEntity:
        await self.session.commit()
        await self.session.refresh(user_buy_list)
        return user_buy_list

    async def delete(self, user_buy_list_id: int) -> bool:
        user_buy_list = await self.get_by_id(user_buy_list_id)
        if user_buy_list:
            await self.session.delete(user_buy_list)
            await self.session.commit()
            return True
        return False

    async def delete_by_user_and_list(self, user_id: int, buy_list_id: int) -> bool:
        query = select(UserBuyListsEntity).where(
            UserBuyListsEntity.user_id == user_id,
            UserBuyListsEntity.buy_list_id == buy_list_id
        )
        result = await self.session.execute(query)
        user_buy_list = result.scalars().first()
        
        if user_buy_list:
            await self.session.delete(user_buy_list)
            await self.session.commit()
            return True
        return False