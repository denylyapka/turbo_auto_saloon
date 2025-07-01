from typing import List, Dict, Optional
from app.models.dtoModels.Entity import Entity


class DiscountDTO(Entity):
    id: int
    car_id: int
    detail_id: int
    name_discount: Optional[str]
    description: Optional[str]
    media_urls: Optional[list[str]]
    discount: float
    for_user: Optional[int]