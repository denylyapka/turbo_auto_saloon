from typing import Optional
from app.models.dtoModels.Entity import Entity


class DimensionsDTO(Entity):
    id: int
    clearance: int
    width: int
    height: int
    length: int
    wheelbase: int
    front_track: int
    rear_track: int
    car_id: Optional[int] = None