from typing import Any, Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.DiscountRepository import DiscountRepository
from app.models.dbModels.Discounts.DiscountEntity import DiscountEntity as Discount
from app.models.dtoModels.DiscountDTO import DiscountDTO


class DiscountService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = DiscountRepository(self.session)

    async def get_all(self) -> list[dict]:
        return await self.repository.get_all()
    
    async def get_cars(self) -> list[dict]:
        return await self.repository.get_all_cars()
    
    async def get_details(self) -> list[dict]:
        return await self.repository.get_all_details()
    
    async def get_by_id(self, discount_id: int) -> Optional[dict]:
        return await self.repository.get_by_id(discount_id)
    
    async def get_by_car_id(self, car_id: int) -> Optional[dict]:
        return await self.repository.get_by_car_id(car_id)
    
    async def get_by_detail_id(self, detail_id: int) -> Optional[dict]:
        return await self.repository.get_by_detail_id(detail_id)
    
    async def get_by_discount_percents(self, discount: int) -> Optional[dict]:
        return await self.repository.get_by_discount_percents(discount)
    
    async def get_by_for_user_id(self, for_user: int) -> Optional[dict]:
        return await self.repository.get_by_for_user_id(for_user)
    
    async def create(self, discount: DiscountDTO) -> Discount:
        discount_data = Discount(
            car_id=discount.car_id,
            detail_id=discount.detail_id,
            name_discount=discount.name_discount,
            description=discount.description,
            media_urls=discount.media_urls,
            discount=discount.discount,
            for_user=discount.for_user
        )
        return await self.repository.create(discount=discount_data)
    
    async def update(self, discount_id: int, discount: DiscountDTO) -> Discount:
        discount_data = Discount(
            car_id=discount.car_id,
            detail_id=discount.detail_id,
            name_discount=discount.name_discount,
            description=discount.description,
            media_urls=discount.media_urls,
            discount=discount.discount,
            for_user=discount.for_user
        )
        return await self.repository.update(discount_id, discount_data)
    
    async def delete(self, discount_id: int) -> bool:
        return await self.repository.delete(discount_id)
    