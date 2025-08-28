from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.ServiceRepository import ServiceRepository
from app.models.dbModels.Services.ServiceEntity import ServiceEntity


class ServiceService:
    def __init__(self, session: AsyncSession):
        self.repo = ServiceRepository(session)
        self.session = session

    async def get_by_id(self, service_id: int) -> ServiceEntity:
        return await self.repo.get_by_id(service_id=service_id)

    async def get_all(self) -> Any:
        return await self.repo.get_all()

    async def create(self, service: ServiceEntity) -> dict:
        return await self.repo.create(service=service)

    async def update(self, service: ServiceEntity) -> dict:
        existing = await self.repo.get_by_id(service.id)
        if not existing:
            raise HTTPException(status_code=404, detail="Service not found")
        return await self.repo.update(service=service)

    async def delete(self, service_id: int) -> bool:
        return await self.repo.delete(service_id=service_id)
