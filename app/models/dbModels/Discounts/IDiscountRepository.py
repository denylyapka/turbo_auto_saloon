from typing import Optional
from app.models.dbModels.Discounts.DiscountEntity import DiscountEntity

class IDiscountRepository:
    async def create(self, discount: DiscountEntity) -> DiscountEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, discount_id: int) -> Optional[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_car_id(self, car_id: int) -> Optional[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_detail_id(self, detail_id: int) -> Optional[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_for_user_id(self, for_user: int) -> Optional[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_discount_percents(self, discount: int) -> Optional[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, discount_id: int, discount_data: dict) -> Optional[DiscountEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, discount_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_cars(self) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_details(self) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_car_id(self, car_id: int) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_detail_id(self, detail_id: int) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_for_user_id(self, for_user: int) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all_by_discount_percents(self, discount: int) -> list[dict]:
        raise NotImplementedError("Метод не реализован!")