from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarEngine import CarEngine

class ICarEngineRepository:
    async def create(self, engine: CarEngine) -> CarEngine:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, engine_id: int) -> Optional[CarEngine]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarEngine]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, engine_id: int, engine_data: dict) -> Optional[CarEngine]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, engine_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")