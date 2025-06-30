from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarEntity import CarEntity
from app.models.dbModels.Cars.IRepositories.ICarEntityRepository import ICarRepository

class CarRepository(ICarRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, car: CarEntity) -> CarEntity:
        self.session.add(car)
        await self.session.commit()
        await self.session.refresh(car)
        return car
    
    async def get_by_id(self, car_id: int) -> Optional[CarEntity]:
        query = select(CarEntity).where(CarEntity.id == car_id)
        result = await self.session.execute(query)
        car = result.scalars().first()
        return car.to_dict() if car else None
    
    async def get_all(self) -> List[CarEntity]:
        query = select(CarEntity)
        result = await self.session.execute(query)
        cars = result.scalars().all()
        return [car.to_dict() for car in cars]
    
    async def get_by_vin(self, vin: str) -> Optional[CarEntity]:
        query = select(CarEntity).where(CarEntity.vin_id == vin)
        result = await self.session.execute(query)
        car = result.scalars().first()
        return car.to_dict() if car else None
    
    async def get_by_brand_model(self, brand: str, model: str) -> List[CarEntity]:
        query = select(CarEntity).where(
            CarEntity.brand == brand,
            CarEntity.model == model
        )
        result = await self.session.execute(query)
        cars = result.scalars().all()
        return [car.to_dict() for car in cars]
    
    async def update(self, car_id: int, car_data: dict) -> Optional[CarEntity]:
        query = select(CarEntity).where(CarEntity.id == car_id)
        result = await self.session.execute(query)
        car = result.scalars().first()
        
        if not car:
            return None
            
        for key, value in car_data.items():
            setattr(car, key, value)
            
        await self.session.commit()
        await self.session.refresh(car)
        return car.to_dict()
    
    async def delete(self, car_id: int) -> bool:
        query = select(CarEntity).where(CarEntity.id == car_id)
        result = await self.session.execute(query)
        car = result.scalars().first()
        
        if not car:
            return False
            
        await self.session.delete(car)
        await self.session.commit()
        return True