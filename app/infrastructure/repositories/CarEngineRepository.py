from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from app.models.dbModels.Cars.Entities.CarEngine import CarEngine
from app.models.dbModels.Cars.IRepositories.ICarEngineRepository import ICarEngineRepository

class CarEngineRepository(ICarEngineRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, engine: CarEngine) -> CarEngine:
        self.session.add(engine)
        await self.session.commit()
        await self.session.refresh(engine)
        return engine
    
    async def get_all(self) -> list[dict]:
        query = select(CarEngine)
        result = await self.session.execute(query)
        engines = result.scalars().all()
        return [engine.to_dict() for engine in engines]
    
    async def get_by_id(self, engine_id: int) -> Optional[CarEngine]:
        query = select(CarEngine).where(CarEngine.id == engine_id)
        result = await self.session.execute(query)
        engine = result.scalars().first()
        return engine.to_dict() if engine else None
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarEngine]:
        query = select(CarEngine).where(CarEngine.car_id == car_id)
        result = await self.session.execute(query)
        engine = result.scalars().first()
        return engine.to_dict() if engine else None
    
    async def update(self, engine_id: int, engine_data: CarEngine) -> Optional[dict]:
        """Обновить данные двигателя автомобиля"""
        query = select(CarEngine).where(CarEngine.id == engine_id)
        result = await self.session.execute(query)
        engine = result.scalars().first()
        
        if not engine:
            raise HTTPException(status_code=404, detail="ВАТАФАК engine")
            
        for field in vars(engine_data):
            if not field.startswith('_') and hasattr(engine, field):
                value = getattr(engine_data, field)
                if value is not None:
                    setattr(engine, field, value)
        
        self.session.add(engine)
        await self.session.commit()
        await self.session.refresh(engine)
        
        return engine.to_dict() if engine else None
    
    async def delete(self, engine_id: int) -> bool:
        query = select(CarEngine).where(CarEngine.id == engine_id)
        result = await self.session.execute(query)
        engine = result.scalars().first()
        
        if not engine:
            return False
            
        await self.session.delete(engine)
        await self.session.commit()
        return True