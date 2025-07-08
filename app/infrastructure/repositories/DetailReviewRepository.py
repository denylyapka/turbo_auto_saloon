from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

from app.models.dbModels.Details.Entities.ReviewEntity import ReviewEntity
from app.models.dbModels.Details.IRepositories.IReviewRepository import IReviewRepository


class ReviewRepository(IReviewRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def check(self, review: ReviewEntity) -> bool:
        query = select(ReviewEntity).where((ReviewEntity.part_id == review.part_id) & (ReviewEntity.user_id == review.user_id))
        result = await self.session.execute(query)
        existing_review = result.scalars().first()
        return existing_review is not None
    
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
    
    async def get_avg_rating(self, part_id: int) -> float:
        # Используем func.avg для вычисления среднего значения
        result = await self.session.execute(
            select(func.avg(ReviewEntity.rating))
            .where(ReviewEntity.part_id == part_id)
        )
        avg = result.scalar() or 0  # Возвращаем 0 если нет отзывов
        return round(float(avg), 2)  # Округляем до 2 знаков
    
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
        # Проверяем, существует ли отзыв в базе
        existing_review = await self.session.get(ReviewEntity, review.id)
        if not existing_review:
            return None

        try:
            # Обновляем все изменяемые поля (кроме id)
            for attr in ['part_id', 'user_id', 'rating', 'comment']:
                if hasattr(review, attr):
                    setattr(existing_review, attr, getattr(review, attr))
            
            await self.session.commit()
            await self.session.refresh(existing_review)
            return existing_review.to_dict()
        except Exception as e:
            await self.session.rollback()
            raise ValueError(f"Failed to update review: {str(e)}") from e
    
    async def delete(self, review_id: int) -> bool:
        query = select(ReviewEntity).where(ReviewEntity.id == review_id)
        result = await self.session.execute(query)
        review = result.scalars().first()
        if review:
            await self.session.delete(review)
            await self.session.commit()
            return True
        return False