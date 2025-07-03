from app.models.dtoModels.Entity import Entity
from typing import List, Dict, Optional


class BuyListsDTO(Entity):
    type: str
    products: List[Dict]
    total_price: int
    total_discount: Optional[int] = None
