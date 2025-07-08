from typing import Optional, List
from app.models.dbModels.Details.Entities.CrossReferencesEntity import CrossReference


class ICrossReferenceRepository:
    async def create(self, cross_ref: CrossReference) -> CrossReference:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, cross_ref_id: int) -> Optional[CrossReference]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[CrossReference]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_part_id(self, part_id: int) -> List[CrossReference]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_brand_and_number(self, brand: str, number: str) -> List[CrossReference]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, cross_ref: CrossReference) -> CrossReference:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, cross_ref_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete_by_part_id(self, part_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")
