from pydantic import BaseModel
from typing import Optional


class BrandDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
