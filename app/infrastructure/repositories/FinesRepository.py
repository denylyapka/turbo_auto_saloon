from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from typing import Optional, List

from app.models.dbModels.Fines.FinesEntity import FinesEntity
from app.models.dbModels.Fines.IFinesRepository import IFinesRepository


class FinesRepository(IFinesRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, fine: FinesEntity) -> FinesEntity:
        self.session.add(fine)
        await self.session.commit()
        await self.session.refresh(fine)
        return fine
    
    async def get_by_id(self, fine_id: int) -> Optional[FinesEntity]:
        query = select(FinesEntity).where(FinesEntity.id == fine_id)
        result = await self.session.execute(query)
        fine = result.scalars().first()
        return fine.to_dict() if fine else None
    
    async def get_all(self) -> List[FinesEntity]:
        query = select(FinesEntity)
        result = await self.session.execute(query)
        fines = result.scalars().all()
        return [fine.to_dict() for fine in fines]
    