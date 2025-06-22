from typing import Optional, List
from datetime import datetime
from app.models.dbModels.BuyLists.BuyListsEntity import BuyListsEntity

class IBuyListsRepository:
    async def create(self, buy_list: BuyListsEntity) -> BuyListsEntity:
        """Создать новый список покупок"""
        raise NotImplementedError("Метод не реализован!")

    async def get_by_id(self, list_id: int) -> Optional[BuyListsEntity]:
        """Получить список по ID"""
        raise NotImplementedError("Метод не реализован!")

    async def get_by_type(self, list_type: str) -> List[BuyListsEntity]:
        """Получить списки по типу"""
        raise NotImplementedError("Метод не реализован!")

    async def get_all(self) -> List[BuyListsEntity]:
        """Получить все списки покупок"""
        raise NotImplementedError("Метод не реализован!")

    async def update(self, buy_list: BuyListsEntity) -> BuyListsEntity:
        """Обновить список покупок"""
        raise NotImplementedError("Метод не реализован!")

    async def delete(self, list_id: int) -> bool:
        """Удалить список по ID"""
        raise NotImplementedError("Метод не реализован!")

    async def search(
        self,
        list_type: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None
    ) -> List[BuyListsEntity]:
        """Поиск списков по параметрам"""
        raise NotImplementedError("Метод не реализован!")