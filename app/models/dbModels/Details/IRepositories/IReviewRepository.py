from typing import Optional, List
from app.models.dbModels.Details.Entities.ReviewEntity import ReviewEntity


class IReviewRepository:
    async def create(self, review: ReviewEntity) -> ReviewEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_id(self, review_id: int) -> Optional[ReviewEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_all(self) -> List[ReviewEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_part_id(self, part_id: int) -> List[ReviewEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_user_id(self, user_id: int) -> List[ReviewEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def get_by_rating_range(self, min_rating: int, max_rating: int) -> List[ReviewEntity]:
        raise NotImplementedError("Метод не реализован!")
    
    async def update(self, review: ReviewEntity) -> ReviewEntity:
        raise NotImplementedError("Метод не реализован!")
    
    async def delete(self, review_id: int) -> bool:
        raise NotImplementedError("Метод не реализован!")