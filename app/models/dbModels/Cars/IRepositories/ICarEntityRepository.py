from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarEntity import CarEntity

class ICarRepository:
    async def create(self, car: CarEntity) -> CarEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, car_id: int) -> Optional[CarEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[CarEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_vin(self, vin: str) -> Optional[CarEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_brand_model(self, brand: str, model: str) -> List[CarEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, car_id: int, car_data: dict) -> Optional[CarEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, car_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")