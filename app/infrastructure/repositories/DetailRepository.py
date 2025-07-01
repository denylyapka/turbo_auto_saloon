from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Details.Entities.DetailEntity import DetailEntity
from app.models.dbModels.Details.IRepositories.IDetailRepository import IDetailRepository


class DetailRepository(IDetailRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, detail: DetailEntity) -> DetailEntity:
        self.session.add(detail)
        await self.session.commit()
        await self.session.refresh(detail)
        return detail
    
    async def get_by_id(self, detail_id: int) -> Optional[DetailEntity]:
        query = select(DetailEntity).where(DetailEntity.id == detail_id)
        result = await self.session.execute(query)
        detail = result.scalars().first()
        return detail.to_dict() if detail else None
    
    async def get_all(self) -> List[DetailEntity]:
        query = select(DetailEntity)
        result = await self.session.execute(query)
        details = result.scalars().all()
        return [detail.to_dict() for detail in details] if details else []
    
    async def get_by_part_number(self, part_number: str) -> Optional[DetailEntity]:
        query = select(DetailEntity).where(DetailEntity.part_number == part_number)
        result = await self.session.execute(query)
        detail = result.scalars().first()
        return detail.to_dict() if detail else None
    
    async def get_by_oem_number(self, oem_number: str) -> List[DetailEntity]:
        query = select(DetailEntity).where(DetailEntity.oem_number == oem_number)
        result = await self.session.execute(query)
        details = result.scalars().all()
        return [detail.to_dict() for detail in details] if details else []
    
    async def get_by_brand(self, brand_id: int) -> List[DetailEntity]:
        query = select(DetailEntity).where(DetailEntity.brand_id == brand_id)
        result = await self.session.execute(query)
        details = result.scalars().all()
        return [detail.to_dict() for detail in details] if details else []
    
    async def get_by_category(self, category_id: int) -> List[DetailEntity]:
        query = select(DetailEntity).where(DetailEntity.category_id == category_id)
        result = await self.session.execute(query)
        details = result.scalars().all()
        return [detail.to_dict() for detail in details] if details else []
    
    async def update(self, detail: DetailEntity) -> DetailEntity:
        await self.session.commit()
        await self.session.refresh(detail)
        return detail.to_dict() if detail else None
    
    async def delete(self, detail_id: int) -> bool:
        query = select(DetailEntity).where(DetailEntity.id == detail_id)
        result = await self.session.execute(query)
        detail = result.scalars().first()
        if detail:
            await self.session.delete(detail)
            await self.session.commit()
            return True
        return False