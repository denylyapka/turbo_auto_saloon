from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Details.Entities.BrandEntity import Brand
from app.models.dbModels.Details.Entities.DetailEntity import DetailEntity as Detail
from app.models.dbModels.Details.IRepositories.IBrandRepository import IBrandRepository


class BrandRepository(IBrandRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, brand: Brand) -> Brand:
        self.session.add(brand)
        await self.session.commit()
        await self.session.refresh(brand)
        return brand
    
    async def get_by_id(self, brand_id: int) -> Optional[Brand]:
        query = select(Brand).where(Brand.id == brand_id)
        result = await self.session.execute(query)
        brand = result.scalars().first()
        return brand.to_dict() if brand else None
    
    async def get_all(self) -> List[Brand]:
        query = select(Brand)
        result = await self.session.execute(query)
        brands = result.scalars().all()
        return [brand.to_dict() for brand in brands] if brands else []
    
    async def get_by_name(self, name: str) -> Optional[Brand]:
        query = select(Brand).where(Brand.name == name)
        result = await self.session.execute(query)
        brand = result.scalars().first()
        return brand.to_dict() if brand else None
    
    async def update(self, brand: Brand) -> Brand:
        await self.session.commit()
        await self.session.refresh(brand)
        return brand.to_dict() if brand else None
    
    async def delete(self, brand_id: int) -> bool:
        query = select(Brand).where(Brand.id == brand_id)
        result = await self.session.execute(query)
        brand = result.scalars().first()
        
        if not brand:
            return False
            
        await self.session.delete(brand)
        await self.session.commit()
        return True
    
    async def transfer_details(self, from_brand_id: int, to_brand_id: int) -> bool:
        query = select(Detail).where(Detail.brand_id == from_brand_id)
        result = await self.session.execute(query)
        brands = result.scalars().all()

        if to_brand_id:
            if brands:
                for brand in brands:
                    brand.brand_id = to_brand_id
                await self.session.commit()
                return True
            return False
        
        print("brands:", brands)
        if brands:
            for brand in brands:
                print("brand:", brand.to_dict())
                await self.session.delete(brand)
                await self.session.commit()
            return True
