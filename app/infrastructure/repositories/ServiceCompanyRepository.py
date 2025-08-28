from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from typing import List, Optional

from app.models.dbModels.ServiceCompanies.Entities.ServiceCompanyEntity import ServiceCompanyEntity


class ServiceCompanyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, sc: ServiceCompanyEntity) -> ServiceCompanyEntity:
        self.session.add(sc)
        await self.session.commit()
        await self.session.refresh(sc)
        return sc

    async def get_by_id(self, sc_id: int) -> Optional[ServiceCompanyEntity]:
        query = select(ServiceCompanyEntity).where(
            ServiceCompanyEntity.id == sc_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[ServiceCompanyEntity]:
        query = select(ServiceCompanyEntity)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, sc: ServiceCompanyEntity) -> Optional[ServiceCompanyEntity]:
        existing = await self.get_by_id(sc.id)
        if not existing:
            return None
        existing.service_id = sc.service_id
        existing.company_id = sc.company_id
        await self.session.commit()
        await self.session.refresh(existing)
        return existing

    async def delete(self, sc_id: int) -> bool:
        existing = await self.get_by_id(sc_id)
        if not existing:
            return False
        await self.session.delete(existing)
        await self.session.commit()
        return True
