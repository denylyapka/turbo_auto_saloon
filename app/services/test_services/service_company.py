from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.ServiceCompanyRepository import ServiceCompanyRepository
from app.models.dbModels.ServiceCompanies.Entities.ServiceCompanyEntity import ServiceCompanyEntity


class ServiceCompanyService:
    def __init__(self, session: AsyncSession):
        self.repo = ServiceCompanyRepository(session)
        self.session = session

    async def get_by_id(self, sc_id: int) -> ServiceCompanyEntity:
        return await self.repo.get_by_id(sc_id=sc_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def create(self, sc: ServiceCompanyEntity) -> dict:
        return await self.repo.create(sc=sc)

    async def update(self, sc: ServiceCompanyEntity) -> dict:
        existing = await self.repo.get_by_id(sc.id)
        if not existing:
            raise HTTPException(
                status_code=404, detail="ServiceCompany not found")
        return await self.repo.update(sc=sc)

    async def delete(self, sc_id: int) -> bool:
        return await self.repo.delete(sc_id=sc_id)
