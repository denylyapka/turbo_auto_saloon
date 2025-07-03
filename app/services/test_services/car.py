from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession


from app.infrastructure.repositories.CarEntityRepository import CarRepository
from app.models.dbModels.Cars.Entities.CarEntity import CarEntity as Car

from app.infrastructure.repositories.CarChassisRepository import CarChassisRepository
from app.models.dbModels.Cars.Entities.CarChassis import CarChassis as Chassis

from app.infrastructure.repositories.CarEngineRepository import CarEngineRepository
from app.models.dbModels.Cars.Entities.CarEngine import CarEngine as Engine

from app.infrastructure.repositories.CarDimensionsRepository import CarDimensionsRepository
from app.models.dbModels.Cars.Entities.CarDimensions import CarDimensions as Dimensions

from app.infrastructure.repositories.CarInteriorRepository import CarInteriorRepository
from app.models.dbModels.Cars.Entities.CarInterior import CarInterior as Interior


class CarEntityService:
    def __init__(self, session: AsyncSession):
        self.repo = CarRepository(session)    
        self.session = session

    async def create(self, car: Car) -> Any:
        return await self.repo.create(car)
    
    async def get_by_id(self, car_id: int) -> Any:
        return await self.repo.get_by_id(car_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_vin(self, vin: str) -> Any:
        return await self.repo.get_by_vin(vin)
        
    async def update(self, car_id: int, car_data: Car) -> Any:
        print(f"3. Calling update with car_id={car_id} Должно быть 2")  # Должно быть 2
        return await self.repo.update(car_id, car_data)
    
    async def delete(self, car_id: int) -> Any:
        return await self.repo.delete(car_id)
    
    async def get_by_filters(self, filters: Any) -> Any:
        return await self.repo.get_by_filters(filters)
    
class ChassisService:
    def __init__(self, session: AsyncSession):
        self.repo = CarChassisRepository(session)
        self.session = session
    
    async def create(self, chassis: Chassis) -> Any:
        return await self.repo.create(chassis)
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, chassis_id: int) -> Any:
        return await self.repo.get_by_id(chassis_id)
    
    async def get_by_car_id(self, car_id: int) -> Any:
        return await self.repo.get_by_car_id(car_id)
    
    async def update(self, chassis_id: int, chassis_data: Chassis) -> Any:
        return await self.repo.update(chassis_id, chassis_data)
    
    async def delete(self, chassis_id: int) -> Any:
        return await self.repo.delete(chassis_id)
    
class EngineService:
    def __init__(self, session: AsyncSession):
        self.repo = CarEngineRepository(session)
        self.session = session
    
    async def create(self, engine: Engine) -> Any:
        return await self.repo.create(engine)
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, engine_id: int) -> Any:
        return await self.repo.get_by_id(engine_id)
    
    async def get_by_car_id(self, car_id: int) -> Any:
        return await self.repo.get_by_car_id(car_id)
    
    async def update(self, engine_id: int, engine_data: Engine) -> Any:
        return await self.repo.update(engine_id, engine_data)
    
    async def delete(self, engine_id: int) -> Any:
        return await self.repo.delete(engine_id)

class DimensionsService:
    def __init__(self, session: AsyncSession):
        self.repo = CarDimensionsRepository(session)
        self.session = session
    
    async def create(self, dimensions: Dimensions) -> Any:
        return await self.repo.create(dimensions)
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, dimensions_id: int) -> Any:
        return await self.repo.get_by_id(dimensions_id)
    
    async def get_by_car_id(self, car_id: int) -> Any:
        return await self.repo.get_by_car_id(car_id)
    
    async def update(self, dimensions_id: int, dimensions_data: Dimensions) -> Any:
        return await self.repo.update(dimensions_id, dimensions_data)
    
    async def delete(self, dimensions_id: int) -> Any:
        return await self.repo.delete(dimensions_id)

class InteriorService:
    def __init__(self, session: AsyncSession):
        self.repo = CarInteriorRepository(session)
        self.session = session
    
    async def create(self, interior: Interior) -> Any:
        return await self.repo.create(interior)
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, interior_id: int) -> Any:
        return await self.repo.get_by_id(interior_id)
    
    async def get_by_car_id(self, car_id: int) -> Any:
        return await self.repo.get_by_car_id(car_id)
    
    async def update(self, interior_id: int, interior_data: Interior) -> Any:
        return await self.repo.update(interior_id, interior_data)
    
    async def delete(self, interior_id: int) -> Any:
        return await self.repo.delete(interior_id)
