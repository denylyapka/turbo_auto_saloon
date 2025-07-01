from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Discounts.DiscountEntity import DiscountEntity
from app.models.dbModels.Discounts.IDiscountRepository import IDiscountRepository


class DiscountRepository(IDiscountRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, discount: DiscountEntity) -> DiscountEntity:
        self.session.add(discount)
        await self.session.commit()
        await self.session.refresh(discount)
        return discount
    
    async def get_by_id(self, discount_id: int) -> Optional[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.id == discount_id)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        return fine.to_dict() if fine else None
    
    async def get_by_car_id(self, car_id: int) -> Optional[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.car_id == car_id)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        return fine.to_dict() if fine else None
    
    async def get_by_detail_id(self, detail_id: int) -> Optional[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.detail_id == detail_id)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        return fine.to_dict() if fine else None
    
    async def get_by_for_user_id(self, for_user: int) -> Optional[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.for_user == for_user)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        return fine.to_dict() if fine else None
    
    async def get_by_discount_percents(self, discount: int) -> Optional[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.discount == discount)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        return fine.to_dict() if fine else None
    
    async def update(self, discount_id: int, discount_data: dict) -> Optional[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.id == discount_id)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        if fine:
            for key, value in discount_data.items():
                setattr(fine, key, value)
            await self.session.commit()
            await self.session.refresh(fine)
            return fine.to_dict()
        return None
    
    async def delete(self, discount_id: int) -> bool:
        query = select(DiscountEntity).where(DiscountEntity.id == discount_id)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        if fine:
            self.session.delete(fine)
            await self.session.commit()
            return True
        return False
    
    async def get_all(self) -> List[DiscountEntity]:
        query = select(DiscountEntity)
        result = await self.session.execute(query)
        fines = result.scalars().all()
        return [fine.to_dict() for fine in fines]
    
    async def get_all_by_car_id(self, car_id: int) -> List[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.car_id == car_id)
        result = await self.session.execute(query)
        fines = result.scalars().all()
        return [fine.to_dict() for fine in fines]
    
    async def get_all_by_detail_id(self, detail_id: int) -> List[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.detail_id == detail_id)
        result = await self.session.execute(query)
        fines = result.scalars().all()
        return [fine.to_dict() for fine in fines]
    
    async def get_all_by_for_user_id(self, for_user: int) -> List[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.for_user == for_user)
        result = await self.session.execute(query)
        fines = result.scalars().all()
        return [fine.to_dict() for fine in fines]
    
    async def get_all_by_discount_percents(self, discount: int) -> List[DiscountEntity]:
        query = select(DiscountEntity).where(DiscountEntity.discount == discount)
        result = await self.session.execute(query)
        fines = result.scalars().all()
        return [fine.to_dict() for fine in fines]
