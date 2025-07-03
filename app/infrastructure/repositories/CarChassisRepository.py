from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from app.models.dbModels.Cars.Entities.CarChassis import CarChassis
from app.models.dbModels.Cars.IRepositories.ICarChassisRepository import ICarChassisRepository

class CarChassisRepository(ICarChassisRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, chassis: CarChassis) -> CarChassis:
        self.session.add(chassis)
        await self.session.commit()
        await self.session.refresh(chassis)
        return chassis
    
    async def get_all(self) -> list[CarChassis]:
        query = select(CarChassis)
        result = await self.session.execute(query)
        chassis = result.scalars().all()
        return [chassis.to_dict() for chassis in chassis] if chassis else None
    
    async def get_by_id(self, chassis_id: int) -> Optional[CarChassis]:
        query = select(CarChassis).where(CarChassis.id == chassis_id)
        result = await self.session.execute(query)
        chassis = result.scalars().first()
        return chassis.to_dict() if chassis else None
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarChassis]:
        query = select(CarChassis).where(CarChassis.car_id == car_id)
        result = await self.session.execute(query)
        chassis = result.scalars().first()
        return chassis.to_dict() if chassis else None
    
    async def update(self, chassis_id: int, chassis_data: CarChassis) -> Optional[dict]:
        """Обновить данные шасси автомобиля"""
        print(f"Repo type: {type(self)}")  # Должно быть CarChassisRepository
        query = select(CarChassis).where(CarChassis.id == chassis_id)
        result = await self.session.execute(query)
        chassis = result.scalars().first()
        
        if not chassis:
            raise HTTPException(status_code=404, detail="ВАТАФАК chassis")
            
        for field in vars(chassis_data):
            if not field.startswith('_') and hasattr(chassis, field):
                value = getattr(chassis_data, field)
                if value is not None:
                    setattr(chassis, field, value)
        
        self.session.add(chassis)
        await self.session.commit()
        await self.session.refresh(chassis)
        
        return chassis.to_dict() if chassis else None
    
    async def delete(self, chassis_id: int) -> bool:
        query = select(CarChassis).where(CarChassis.id == chassis_id)
        result = await self.session.execute(query)
        chassis = result.scalars().first()
        
        if not chassis:
            return False
            
        await self.session.delete(chassis)
        await self.session.commit()
        return True