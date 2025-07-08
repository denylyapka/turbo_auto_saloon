from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Details.Entities.CompatibilityEntity import Compatibility
from app.models.dbModels.Details.IRepositories.ICompatibilityRepository import ICompatibilityRepository


class CompatibilityRepository(ICompatibilityRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, compatibility: Compatibility) -> Compatibility:
        self.session.add(compatibility)
        await self.session.commit()
        await self.session.refresh(compatibility)
        return compatibility
    
    async def get_by_id(self, compatibility_id: int) -> Optional[Compatibility]:
        query = select(Compatibility).where(Compatibility.id == compatibility_id)
        result = await self.session.execute(query)
        compatibility = result.scalars().first()
        return compatibility.to_dict() if compatibility else None
    
    async def get_all(self) -> List[Compatibility]:
        query = select(Compatibility)
        result = await self.session.execute(query)
        compatibilities = result.scalars().all()
        return [compatibility.to_dict() for compatibility in compatibilities] if compatibilities else []
    
    async def get_by_part_id(self, part_id: int) -> List[Compatibility]:
        query = select(Compatibility).where(Compatibility.part_id == part_id)
        result = await self.session.execute(query)
        compatibilities = result.scalars().all()
        return [compatibility.to_dict() for compatibility in compatibilities] if compatibilities else []
    
    async def get_by_vehicle(self, make: str, model: str, year: int) -> List[Compatibility]:
        query = select(Compatibility).where(
            (Compatibility.make == make) &
            (Compatibility.model == model) &
            (Compatibility.year_from <= year) &
            (Compatibility.year_to >= year))
        result = await self.session.execute(query)
        compatibilities = result.scalars().all()
        return [compatibility.to_dict() for compatibility in compatibilities] if compatibilities else []
    
    async def update(self, compatibility: Compatibility) -> Compatibility:
        await self.session.commit()
        await self.session.refresh(compatibility)
        return compatibility.to_dict() if compatibility else None
    
    async def delete(self, compatibility_id: int) -> bool:
        query = select(Compatibility).where(Compatibility.id == compatibility_id)
        result = await self.session.execute(query)
        compatibility = result.scalars().first()
        if compatibility:
            await self.session.delete(compatibility)
            await self.session.commit()
            return True
        return False
    
    async def delete_by_detail_id(self, detail_id: int) -> bool:
        query = select(Compatibility).where(Compatibility.part_id == detail_id)
        result = await self.session.execute(query)
        compatibilities = result.scalars().all()

        # print("compatibilities:", compatibilities)
        # for compatibility in compatibilities:
        #     print("compatibility:", compatibility.to_dict())
        # return compatibilities
        if compatibilities:
            for compatibility in compatibilities:
                await self.session.delete(compatibility)
            await self.session.commit()
            return True
        return False