from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from typing import List, Optional

from app.models.dbModels.Categories.CategoryHierarchyEntity import CategoryHierarchyEntity


class CategoryHierarchyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, hierarchy: CategoryHierarchyEntity) -> CategoryHierarchyEntity:
        self.session.add(hierarchy)
        await self.session.commit()
        await self.session.refresh(hierarchy)
        return hierarchy

    async def get_by_id(self, hierarchy_id: int) -> Optional[CategoryHierarchyEntity]:
        query = select(CategoryHierarchyEntity).where(
            CategoryHierarchyEntity.id == hierarchy_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[CategoryHierarchyEntity]:
        query = select(CategoryHierarchyEntity)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, hierarchy: CategoryHierarchyEntity) -> Optional[CategoryHierarchyEntity]:
        existing = await self.get_by_id(hierarchy.id)
        if not existing:
            return None
        existing.name = hierarchy.name
        await self.session.commit()
        await self.session.refresh(existing)
        return existing

    async def delete(self, hierarchy_id: int) -> bool:
        existing = await self.get_by_id(hierarchy_id)
        if not existing:
            return False
        await self.session.delete(existing)
        await self.session.commit()
        return True
