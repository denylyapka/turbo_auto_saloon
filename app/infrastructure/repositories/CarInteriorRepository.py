from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarInterior import CarInterior
from app.models.dbModels.Cars.IRepositories.ICarInteriorRepository import ICarInteriorRepository

class CarInteriorRepository(ICarInteriorRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, interior: CarInterior) -> CarInterior:
        self.session.add(interior)
        await self.session.commit()
        await self.session.refresh(interior)
        return interior
    
    async def get_all(self) -> List[CarInterior]:
        query = select(CarInterior)
        result = await self.session.execute(query)
        interiors = result.scalars().all()
        return [interior.to_dict() for interior in interiors] if interiors else None
    
    async def get_by_id(self, interior_id: int) -> Optional[CarInterior]:
        query = select(CarInterior).where(CarInterior.id == interior_id)
        result = await self.session.execute(query)
        interior = result.scalars().first()
        return interior.to_dict() if interior else None
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarInterior]:
        query = select(CarInterior).where(CarInterior.car_id == car_id)
        result = await self.session.execute(query)
        interior = result.scalars().first()
        return interior.to_dict() if interior else None
    
    async def update(self, interior_id: int, interior_data: CarInterior) -> Optional[dict]:
        """Обновить данные интерьера автомобиля"""
        query = select(CarInterior).where(CarInterior.id == interior_id)
        result = await self.session.execute(query)
        interior = result.scalars().first()
        
        if not interior:
            raise HTTPException(status_code=404, detail="ВАТАФАК interior")
            
        for field in vars(interior_data):
            if not field.startswith('_') and hasattr(interior, field):
                value = getattr(interior_data, field)
                if value is not None:
                    setattr(interior, field, value)
        
        self.session.add(interior)
        await self.session.commit()
        await self.session.refresh(interior)
        
        return interior.to_dict() if interior else None
    
    async def delete(self, interior_id: int) -> bool:
        query = select(CarInterior).where(CarInterior.id == interior_id)
        result = await self.session.execute(query)
        interior = result.scalars().first()
        
        if not interior:
            return False
            
        await self.session.delete(interior)
        await self.session.commit()
        return True
    
    async def get_by_features(self, features: dict) -> List[CarInterior]:
        query = select(CarInterior)
        
        for key, value in features.items():
            if hasattr(CarInterior, key):
                query = query.where(getattr(CarInterior, key) == value)
        
        result = await self.session.execute(query)
        interiors = result.scalars().all()
        return [interior.to_dict() for interior in interiors]