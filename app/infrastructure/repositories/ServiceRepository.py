from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from typing import List, Optional

from app.models.dbModels.Services.ServiceEntity import ServiceEntity


class ServiceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, service: ServiceEntity) -> ServiceEntity:
        self.session.add(service)
        await self.session.commit()
        await self.session.refresh(service)
        return service

    async def get_by_id(self, service_id: int) -> Optional[ServiceEntity]:
        query = select(ServiceEntity).where(ServiceEntity.id == service_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[ServiceEntity]:
        query = select(ServiceEntity)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, service: ServiceEntity) -> Optional[ServiceEntity]:
        existing = await self.get_by_id(service.id)
        if not existing:
            return None
        existing.name = service.name
        await self.session.commit()
        await self.session.refresh(existing)
        return existing

    async def delete(self, service_id: int) -> bool:
        existing = await self.get_by_id(service_id)
        if not existing:
            return False
        await self.session.delete(existing)
        await self.session.commit()
        return True
