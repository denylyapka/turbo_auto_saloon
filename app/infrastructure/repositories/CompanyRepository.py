from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from typing import List, Optional

from app.models.dbModels.Companies.CompanyEntity import CompanyEntity


class CompanyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, company: CompanyEntity) -> CompanyEntity:
        self.session.add(company)
        await self.session.commit()
        await self.session.refresh(company)
        return company

    async def get_by_id(self, company_id: int) -> Optional[CompanyEntity]:
        query = select(CompanyEntity).where(CompanyEntity.id == company_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self) -> List[CompanyEntity]:
        query = select(CompanyEntity)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update(self, company: CompanyEntity) -> Optional[CompanyEntity]:
        existing = await self.get_by_id(company.id)
        if not existing:
            return None
        existing.name = company.name
        await self.session.commit()
        await self.session.refresh(existing)
        return existing

    async def delete(self, company_id: int) -> bool:
        existing = await self.get_by_id(company_id)
        if not existing:
            return False
        await self.session.delete(existing)
        await self.session.commit()
        return True
