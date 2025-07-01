from typing import Optional, List
from app.models.dbModels.Details.Entities.BrandEntity import Brand


class IBrandRepository:
    async def create(self, brand: Brand) -> Brand:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, brand_id: int) -> Optional[Brand]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[Brand]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_name(self, name: str) -> Optional[Brand]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, brand: Brand) -> Brand:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, brand_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")