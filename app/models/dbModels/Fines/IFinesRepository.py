from typing import Optional, List
from datetime import datetime
from app.models.dbModels.Fines.FinesEntity import FinesEntity   


class IFinesRepository:
    async def create(self, fine: FinesEntity) -> FinesEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, fine_id: int) -> Optional[FinesEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[FinesEntity]:
        raise NotImplementedError("Метод не реализован!")