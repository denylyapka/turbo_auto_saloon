from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.CompanyRepository import CompanyRepository
from app.models.dbModels.Companies.CompanyEntity import CompanyEntity


class CompanyService:
    def __init__(self, session: AsyncSession):
        self.repo = CompanyRepository(session)
        self.session = session

    async def get_by_id(self, company_id: int) -> CompanyEntity:
        return await self.repo.get_by_id(company_id=company_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def create(self, company: CompanyEntity) -> dict:
        return await self.repo.create(company=company)

    async def update(self, company: CompanyEntity) -> dict:
        existing = await self.repo.get_by_id(company.id)
        if not existing:
            raise HTTPException(status_code=404, detail="Company not found")
        return await self.repo.update(company=company)

    async def delete(self, company_id: int) -> bool:
        return await self.repo.delete(company_id=company_id)
