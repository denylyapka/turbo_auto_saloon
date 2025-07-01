from typing import Optional, List
from app.models.dbModels.Details.Entities.CategoryEntity import Category


class ICategoryRepository:
    async def create(self, category: Category) -> Category:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, category_id: int) -> Optional[Category]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[Category]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_name(self, name: str) -> Optional[Category]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_children(self, parent_id: int) -> List[Category]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, category: Category) -> Category:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, category_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")