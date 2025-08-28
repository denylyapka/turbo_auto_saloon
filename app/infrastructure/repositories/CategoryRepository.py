from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from typing import List, Optional

from app.models.dbModels.Categories.CategoryEntity import CategoryEntity


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, category: CategoryEntity) -> CategoryEntity:
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def get_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        query = select(CategoryEntity).where(CategoryEntity.id == category_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[CategoryEntity]:
        query = select(CategoryEntity)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, category: CategoryEntity) -> Optional[CategoryEntity]:
        existing = await self.get_by_id(category.id)
        if not existing:
            return None
        existing.category_name = category.category_name
        await self.session.commit()
        await self.session.refresh(existing)
        return existing

    async def delete(self, category_id: int) -> bool:
        existing = await self.get_by_id(category_id)
        if not existing:
            return False
        await self.session.delete(existing)
        await self.session.commit()
        return True
