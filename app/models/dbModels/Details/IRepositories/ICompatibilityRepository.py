from typing import Optional, List
from app.models.dbModels.Details.Entities.CompatibilityEntity import Compatibility


class ICompatibilityRepository:
    async def create(self, compatibility: Compatibility) -> Compatibility:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, compatibility_id: int) -> Optional[Compatibility]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[Compatibility]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_part_id(self, part_id: int) -> List[Compatibility]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_vehicle(self, make: str, model: str, year: int) -> List[Compatibility]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, compatibility: Compatibility) -> Compatibility:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, compatibility_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")