from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class DetailTotalDTO(BaseModel):
    # детали
    name_detail: str
    part_number: str
    oem_number: Optional[str] = None
    brand_id: int
    category_id: int
    price: float
    quantity: int
    weight_kg: Optional[float] = None
    description: Optional[str] = None
    image_urls: Optional[List[str]] = None
    warranty_months: Optional[int] = None
    installation_guide_url: Optional[str] = None
    video_review_url: Optional[str] = None

    # бренды
    name_brand: str
    description: Optional[str] = None
    logo_url: Optional[str] = None

    # категории
    name_category: str
    parent_id: Optional[int] = None

    # совместимость с тачками
    make: str
    model: str
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    engine_type: Optional[str] = None

    # # кросс референсы
    # part_id: int
    # brand: str
    # number: str

    # # отзывы
    # part_id: int
    # user_id: int
    # rating: int
    # comment: Optional[str] = None
    # created_at: datetime
