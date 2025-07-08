from typing import Any, List

from sqlalchemy.ext.asyncio import AsyncSession


from app.infrastructure.repositories.DetailRepository import DetailRepository
from app.models.dbModels.Details.Entities.DetailEntity import DetailEntity as Detail

from app.infrastructure.repositories.DetailBrandRepository import BrandRepository
from app.models.dbModels.Details.Entities.BrandEntity import Brand as Brand

from app.infrastructure.repositories.DetailCategoryRepository import CategoryRepository
from app.models.dbModels.Details.Entities.CategoryEntity import Category as Category

from app.infrastructure.repositories.DetailReviewRepository import ReviewRepository
from app.models.dbModels.Details.Entities.ReviewEntity import ReviewEntity as Review

from app.infrastructure.repositories.DetailCompatibilityRepository import CompatibilityRepository
from app.models.dbModels.Details.Entities.CompatibilityEntity import Compatibility as Compatibility

from app.infrastructure.repositories.DetailCrossReferenceRepository import CrossReferenceRepository
from app.models.dbModels.Details.Entities.CrossReferencesEntity import CrossReference as CrossReference


class DetailService:
    def __init__(self, session: AsyncSession):
        self.repo = DetailRepository(session)    
        self.session = session
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, detail_id: int) -> Any:
        return await self.repo.get_by_id(detail_id)
    
    async def get_by_part_number(self, part_number: str) -> Any:
        return await self.repo.get_by_part_number(part_number)
    
    async def get_by_oem_number(self, oem_number: str) -> Any:
        return await self.repo.get_by_oem_number(oem_number)
    
    async def get_by_brand(self, brand_id: int) -> Any:
        return await self.repo.get_by_brand(brand_id)
    
    async def get_by_category(self, category_id: int) -> List[Detail]:
        return await self.repo.get_by_category(category_id)

    async def create(self, detail: Detail) -> Any:
        return await self.repo.create(detail)
    
    async def update(self, detail: Detail) -> Any:
        return await self.repo.update(detail)
    
    async def delete(self, detail_id: int) -> Any:
        return await self.repo.delete(detail_id)

class BrandService:
    def __init__(self, session: AsyncSession):
        self.repo = BrandRepository(session)    
        self.session = session
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, brand_id: int) -> Any:
        return await self.repo.get_by_id(brand_id)
    
    async def get_by_name(self, name: str) -> Any:
        return await self.repo.get_by_name(name)
    
    async def create(self, brand: Brand) -> Any:
        return await self.repo.create(brand)
    
    async def update(self, brand: Brand) -> Any:
        return await self.repo.update(brand)
    
    async def delete(self, brand_id: int) -> bool:
        return await self.repo.delete(brand_id)
    
    async def transfer_details(self, from_brand_id: int, to_brand_id: int) -> Any:
        return await self.repo.transfer_details(from_brand_id, to_brand_id)
    

class CategoryService:
    def __init__(self, session: AsyncSession):
        self.repo = CategoryRepository(session)    
        self.session = session
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, category_id: int) -> Any:
        return await self.repo.get_by_id(category_id)
    
    async def get_by_name(self, name: str) -> Any:
        return await self.repo.get_by_name(name)
    
    async def create(self, category: Category) -> Category:
        if not category.name:
            raise ValueError("Название категории обязательно")

        return await self.repo.create(category)
    
    async def update(self, category: Category) -> Any:
        return await self.repo.update(category)
    
    async def delete(self, category_id: int) -> Any:
        return await self.repo.delete(category_id)
    
    async def transfer_details(self, from_category_id: int, to_category_id: int) -> Any:
        return await self.repo.transfer_details(from_category_id, to_category_id)


class ReviewService:
    def __init__(self, session: AsyncSession):
        self.repo = ReviewRepository(session)    
        self.session = session
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, review_id: int) -> Any:
        return await self.repo.get_by_id(review_id)
    
    async def get_by_part_id(self, part_id: int) -> Any:
        return await self.repo.get_by_part_id(part_id)
    
    async def get_avg_rating(self, part_id: int) -> Any:
        return await self.repo.get_avg_rating(part_id)
    
    async def get_by_user_id(self, user_id: int) -> Any:
        return await self.repo.get_by_user_id(user_id)
    
    async def get_by_rating_range(self, min_rating: int, max_rating: int) -> Any:
        return await self.repo.get_by_rating_range(min_rating, max_rating)
    
    async def create(self, review: Review) -> Any:
        return await self.repo.create(review)
    
    async def check(self, review: Review) -> Any:
        return await self.repo.check(review)
    
    async def update(self, review: Review) -> Any:
        return await self.repo.update(review)
    
    async def delete(self, review_id: int) -> Any:
        return await self.repo.delete(review_id)


class CompatibilityService:
    def __init__(self, session: AsyncSession):
        self.repo = CompatibilityRepository(session)    
        self.session = session

    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, compatibility_id: int) -> Any:
        return await self.repo.get_by_id(compatibility_id)
    
    async def create(self, compatibility: Compatibility) -> Any:
        return await self.repo.create(compatibility)
    
    async def update(self, compatibility: Compatibility) -> Any:
        return await self.repo.update(compatibility)
    
    async def delete(self, compatibility_id: int) -> Any:
        return await self.repo.delete(compatibility_id)
    
    async def delete_by_detail_id(self, detail_id: int) -> Any:
        return await self.repo.delete_by_detail_id(detail_id)


class CrossReferenceService:
    def __init__(self, session: AsyncSession):
        self.repo = CrossReferenceRepository(session)    
        self.session = session
    
    async def get_all(self) -> Any:
        return await self.repo.get_all()
    
    async def get_by_id(self, cross_ref_id: int) -> Any:
        return await self.repo.get_by_id(cross_ref_id)
    
    async def get_by_part_id(self, part_id: int) -> Any:
        return await self.repo.get_by_part_id(part_id)
    
    async def get_by_brand_and_number(self, brand: str, number: str) -> Any:
        
        return await self.repo.get_by_brand_and_number(brand, number)
    
    async def create(self, cross_ref: CrossReference) -> Any:
        return await self.repo.create(cross_ref)
    
    async def update(self, cross_ref: CrossReference) -> Any:
        return await self.repo.update(cross_ref)
    
    async def delete(self, cross_ref_id: int) -> Any:
        return await self.repo.delete(cross_ref_id)
    
    async def delete_by_part_id(self, part_id: int) -> Any:
        return await self.repo.delete_by_part_id(part_id)
    
    

