from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.CategoryRepository import CategoryRepository
from app.models.dbModels.Categories.CategoryEntity import CategoryEntity


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.repo = CategoryRepository(session)
        self.session = session

    async def get_by_id(self, category_id: int) -> CategoryEntity:
        return await self.repo.get_by_id(category_id=category_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def create(self, category: CategoryEntity) -> dict:
        return await self.repo.create(category=category)

    async def update(self, category: CategoryEntity) -> dict:
        existing = await self.repo.get_by_id(category.id)
        if not existing:
            raise HTTPException(status_code=404, detail="Category not found")
        return await self.repo.update(category=category)

    async def delete(self, category_id: int) -> bool:
        return await self.repo.delete(category_id=category_id)
