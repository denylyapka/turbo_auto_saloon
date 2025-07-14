from app.models.dtoModels.Entity import Entity
from typing import List, Optional

class ProductDTO(Entity):
    type_prod: str
    id_prod: int
    quantity: int

class BuyListsDTO(Entity):
    user_id: int
    type: str
    products: List[ProductDTO]
    total_price: int
    total_discount: Optional[int] = None