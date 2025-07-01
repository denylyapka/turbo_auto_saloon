from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Details.Entities.CategoryEntity import Category
from app.models.dbModels.Details.IRepositories.ICategoryRepository import ICategoryRepository


class CategoryRepository(ICategoryRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, category: Category) -> Category:
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category
    
    async def get_by_id(self, category_id: int) -> Optional[Category]:
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        category = result.scalars().first()
        return category.to_dict() if category else None
    
    async def get_all(self) -> List[Category]:
        query = select(Category)
        result = await self.session.execute(query)
        categories = result.scalars().all()
        return [category.to_dict() for category in categories]
    
    async def get_by_name(self, name: str) -> Optional[Category]:
        query = select(Category).where(Category.name == name)
        result = await self.session.execute(query)
        category = result.scalars().first()
        return category.to_dict() if category else None
    
    async def get_children(self, parent_id: int) -> List[Category]:
        query = select(Category).where(Category.parent_id == parent_id)
        result = await self.session.execute(query)
        categories = result.scalars().all()
        return [category.to_dict() for category in categories]
    
    async def update(self, category: Category) -> Category:
        await self.session.commit()
        await self.session.refresh(category)
        return category.to_dict()
    
    async def delete(self, category_id: int) -> bool:
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        category = result.scalars().first()
        if category:
            await self.session.delete(category)
            await self.session.commit()
            return True
        return False