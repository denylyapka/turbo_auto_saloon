from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict, Optional

class BuyListsBase(BaseModel):
    type: str
    products: List[Dict]
    total_price: int
    total_discount: Optional[int] = None

class BuyListsCreate(BuyListsBase):
    """Схема для создания списка"""
    pass

class BuyListsDTO(BuyListsBase):
    """Основная DTO схема"""
    id: int
    datetime_create: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "type": "electronics",
                "products": [{"name": "Smartphone", "price": 500}],
                "datetime_create": "2023-01-01T00:00:00",
                "total_price": 500,
                "total_discount": 50
            }
        }

class BuyListsResponse(BuyListsDTO):
    """Схема для ответа API"""
    pass

class BuyListsDetailed(BuyListsDTO):
    """Расширенная схема для внутреннего использования"""
    pass