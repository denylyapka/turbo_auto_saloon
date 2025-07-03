from app.models.dtoModels.Entity import Entity
from typing import Optional


class BrandDTO(Entity):
    id: int
    name: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
