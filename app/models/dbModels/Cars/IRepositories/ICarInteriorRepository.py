from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarInterior import CarInterior

class ICarInteriorRepository:
    async def create(self, interior: CarInterior) -> CarInterior:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[CarInterior]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, interior_id: int) -> Optional[CarInterior]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarInterior]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, interior_id: int, interior_data: dict) -> Optional[CarInterior]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, interior_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_features(self, features: dict) -> List[CarInterior]:
        raise NotImplementedError("Метод не реализован!")