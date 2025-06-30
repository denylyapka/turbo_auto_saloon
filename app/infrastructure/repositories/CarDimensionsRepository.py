from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from app.models.dbModels.Cars.Entities.CarDimensions import CarDimensions
from app.models.dbModels.Cars.IRepositories.ICarDimensionsRepository import ICarDimensionsRepository

class CarDimensionsRepository(ICarDimensionsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, dimensions: CarDimensions) -> CarDimensions:
        self.session.add(dimensions)
        await self.session.commit()
        await self.session.refresh(dimensions)
        return dimensions
    
    async def get_by_id(self, dimensions_id: int) -> Optional[CarDimensions]:
        query = select(CarDimensions).where(CarDimensions.id == dimensions_id)
        result = await self.session.execute(query)
        dimensions = result.scalars().first()
        return dimensions.to_dict() if dimensions else None
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarDimensions]:
        query = select(CarDimensions).where(CarDimensions.car_id == car_id)
        result = await self.session.execute(query)
        dimensions = result.scalars().first()
        return dimensions.to_dict() if dimensions else None
    
    async def update(self, dimensions_id: int, dimensions_data: dict) -> Optional[CarDimensions]:
        query = select(CarDimensions).where(CarDimensions.id == dimensions_id)
        result = await self.session.execute(query)
        dimensions = result.scalars().first()
        
        if not dimensions:
            return None
            
        for key, value in dimensions_data.items():
            setattr(dimensions, key, value)
            
        await self.session.commit()
        await self.session.refresh(dimensions)
        return dimensions.to_dict()
    
    async def delete(self, dimensions_id: int) -> bool:
        query = select(CarDimensions).where(CarDimensions.id == dimensions_id)
        result = await self.session.execute(query)
        dimensions = result.scalars().first()
        
        if not dimensions:
            return False
            
        await self.session.delete(dimensions)
        await self.session.commit()
        return True