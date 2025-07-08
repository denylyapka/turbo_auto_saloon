from pydantic import BaseModel
from typing import Optional


class CompatibilityDTO(BaseModel):
    part_id: int
    make: str
    model: str
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    engine_type: Optional[str] = None
