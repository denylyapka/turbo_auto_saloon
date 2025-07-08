from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ReviewDTO(BaseModel):
    part_id: int
    user_id: int
    rating: int
    comment: Optional[str] = None

class ReviewEditModeDTO(BaseModel):
    id: int
    part_id: int
    user_id: int
    rating: int
    comment: Optional[str] = None