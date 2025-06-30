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
    
    async def update(self, interior_id: int, interior_data: dict) -> Optional[CarInterior]:
        query = select(CarInterior).where(CarInterior.id == interior_id)
        result = await self.session.execute(query)
        interior = result.scalars().first()
        
        if not interior:
            return None
            
        for key, value in interior_data.items():
            setattr(interior, key, value)
            
        await self.session.commit()
        await self.session.refresh(interior)
        return interior.to_dict()
    
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