from typing import Optional, List
from app.models.dbModels.UserBuyLists.UserBuyListsEntity import UserBuyListsEntity

class IUserBuyListsRepository:
    async def create(self, user_buy_list: UserBuyListsEntity) -> UserBuyListsEntity:
        """Создать новую связь пользователя и списка покупок"""
        raise NotImplementedError("Метод не реализован!")

    async def get_by_id(self, user_buy_list_id: int) -> Optional[UserBuyListsEntity]:
        """Получить связь по ID"""
        raise NotImplementedError("Метод не реализован!")

    async def get_by_user_id(self, user_id: int) -> List[UserBuyListsEntity]:
        """Получить все списки пользователя"""
        raise NotImplementedError("Метод не реализован!")

    async def get_by_buy_list_id(self, buy_list_id: int) -> List[UserBuyListsEntity]:
        """Получить всех пользователей списка"""
        raise NotImplementedError("Метод не реализован!")

    async def get_all(self) -> List[UserBuyListsEntity]:
        """Получить все связи пользователей и списков"""
        raise NotImplementedError("Метод не реализован!")

    async def update(self, user_buy_list: UserBuyListsEntity) -> UserBuyListsEntity:
        """Обновить связь пользователя и списка"""
        raise NotImplementedError("Метод не реализован!")

    async def delete(self, user_buy_list_id: int) -> bool:
        """Удалить связь по ID"""
        raise NotImplementedError("Метод не реализован!")

    async def delete_by_user_and_list(self, user_id: int, buy_list_id: int) -> bool:
        """Удалить связь пользователя и конкретного списка"""
        raise NotImplementedError("Метод не реализован!")