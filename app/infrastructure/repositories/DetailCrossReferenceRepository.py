from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Details.Entities.CrossReferencesEntity import CrossReference
from app.models.dbModels.Details.IRepositories.ICrossReferenceRepository import ICrossReferenceRepository


class CrossReferenceRepository(ICrossReferenceRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, cross_ref: CrossReference) -> CrossReference:
        self.session.add(cross_ref)
        await self.session.commit()
        await self.session.refresh(cross_ref)
        return cross_ref
    
    async def get_by_id(self, cross_ref_id: int) -> Optional[CrossReference]:
        query = select(CrossReference).where(CrossReference.id == cross_ref_id)
        result = await self.session.execute(query)
        cross_ref = result.scalars().first()
        return cross_ref.to_dict() if cross_ref else None
    
    async def get_all(self) -> List[CrossReference]:
        query = select(CrossReference)
        result = await self.session.execute(query)
        cross_refs = result.scalars().all()
        return [cross_ref.to_dict() for cross_ref in cross_refs] if cross_refs else []
    
    async def get_by_part_id(self, part_id: int) -> List[CrossReference]:
        query = select(CrossReference).where(CrossReference.part_id == part_id)
        result = await self.session.execute(query)
        cross_refs = result.scalars().all()
        return [cross_ref.to_dict() for cross_ref in cross_refs] if cross_refs else []
    
    async def get_by_brand_and_number(self, brand: str, number: str) -> List[CrossReference]:
        query = select(CrossReference).where(
            (CrossReference.brand == brand) &
            (CrossReference.number == number))
        result = await self.session.execute(query)
        cross_refs = result.scalars().all()
        return [cross_ref.to_dict() for cross_ref in cross_refs] if cross_refs else []
    
    async def update(self, cross_ref: CrossReference) -> CrossReference:
        await self.session.commit()
        await self.session.refresh(cross_ref)
        return cross_ref.to_dict() if cross_ref else None
    
    async def delete(self, cross_ref_id: int) -> bool:
        query = select(CrossReference).where(CrossReference.id == cross_ref_id)
        result = await self.session.execute(query)
        cross_ref = result.scalars().first()
        if cross_ref:
            await self.session.delete(cross_ref)
            await self.session.commit()
            return True
        return False