from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.dbModels.Details.Entities.ReviewEntity import ReviewEntity
from app.models.dbModels.Details.IRepositories.IReviewRepository import IReviewRepository


class ReviewRepository(IReviewRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, review: ReviewEntity) -> ReviewEntity:
        self.session.add(review)
        await self.session.commit()
        await self.session.refresh(review)
        return review
    
    async def get_by_id(self, review_id: int) -> Optional[ReviewEntity]:
        query = select(ReviewEntity).where(ReviewEntity.id == review_id)
        result = await self.session.execute(query)
        review = result.scalars().first()
        return review.to_dict() if review else None
    
    async def get_all(self) -> List[ReviewEntity]:
        query = select(ReviewEntity)
        result = await self.session.execute(query)
        reviews = result.scalars().all()
        return [review.to_dict() for review in reviews] if reviews else []
    
    async def get_by_part_id(self, part_id: int) -> List[ReviewEntity]:
        query = select(ReviewEntity).where(ReviewEntity.part_id == part_id)
        result = await self.session.execute(query)
        reviews = result.scalars().all()
        return [review.to_dict() for review in reviews] if reviews else []
    
    async def get_by_user_id(self, user_id: int) -> List[ReviewEntity]:
        query = select(ReviewEntity).where(ReviewEntity.user_id == user_id)
        result = await self.session.execute(query)
        reviews = result.scalars().all()
        return [review.to_dict() for review in reviews] if reviews else []
    
    async def get_by_rating_range(self, min_rating: int, max_rating: int) -> List[ReviewEntity]:
        query = select(ReviewEntity).where(
            (ReviewEntity.rating >= min_rating) &
            (ReviewEntity.rating <= max_rating))
        result = await self.session.execute(query)
        reviews = result.scalars().all()
        return [review.to_dict() for review in reviews] if reviews else []
    
    async def update(self, review: ReviewEntity) -> ReviewEntity:
        await self.session.commit()
        await self.session.refresh(review)
        return review.to_dict() if review else None
    
    async def delete(self, review_id: int) -> bool:
        query = select(ReviewEntity).where(ReviewEntity.id == review_id)
        result = await self.session.execute(query)
        review = result.scalars().first()
        if review:
            await self.session.delete(review)
            await self.session.commit()
            return True
        return False