from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class DetailDTO(BaseModel):
    name: str
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
