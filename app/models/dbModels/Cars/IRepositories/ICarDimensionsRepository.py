from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarDimensions import CarDimensions

class ICarDimensionsRepository:
    async def create(self, dimensions: CarDimensions) -> CarDimensions:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[CarDimensions]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, dimensions_id: int) -> Optional[CarDimensions]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarDimensions]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, dimensions_id: int, dimensions_data: dict) -> Optional[CarDimensions]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, dimensions_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")