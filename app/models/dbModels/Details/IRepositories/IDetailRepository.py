from typing import Optional, List
from app.models.dbModels.Details.Entities.DetailEntity import DetailEntity


class IDetailRepository:
    async def create(self, detail: DetailEntity) -> DetailEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, detail_id: int) -> Optional[DetailEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[DetailEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_part_number(self, part_number: str) -> Optional[DetailEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_oem_number(self, oem_number: str) -> List[DetailEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_brand(self, brand_id: int) -> List[DetailEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_category(self, category_id: int) -> List[DetailEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, detail: DetailEntity) -> DetailEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, detail_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")