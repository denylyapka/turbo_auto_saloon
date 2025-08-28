from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.CategoryHierarchyRepository import CategoryHierarchyRepository
from app.models.dbModels.CategoryHierarchies.Entities.CategoryHierarchyEntity import CategoryHierarchyEntity


class CategoryHierarchyService:
    def __init__(self, session: AsyncSession):
        self.repo = CategoryHierarchyRepository(session)
        self.session = session

    async def get_by_id(self, hierarchy_id: int) -> CategoryHierarchyEntity:
        return await self.repo.get_by_id(hierarchy_id=hierarchy_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def create(self, hierarchy: CategoryHierarchyEntity) -> dict:
        return await self.repo.create(hierarchy=hierarchy)

    async def update(self, hierarchy: CategoryHierarchyEntity) -> dict:
        existing = await self.repo.get_by_id(hierarchy.id)
        if not existing:
            raise HTTPException(
                status_code=404, detail="Category hierarchy not found")
        return await self.repo.update(hierarchy=hierarchy)

    async def delete(self, hierarchy_id: int) -> bool:
        return await self.repo.delete(hierarchy_id=hierarchy_id)
