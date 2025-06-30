from typing import Optional, List
from app.models.dbModels.Cars.Entities.CarChassis import CarChassis

class ICarChassisRepository:
    async def create(self, chassis: CarChassis) -> CarChassis:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, chassis_id: int) -> Optional[CarChassis]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_car_id(self, car_id: int) -> Optional[CarChassis]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, chassis_id: int, chassis_data: dict) -> Optional[CarChassis]:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, chassis_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")