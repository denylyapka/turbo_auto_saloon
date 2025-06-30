from typing import Optional
from app.models.dtoModels.Entity import Entity


class ChassisDTO(Entity):
    id: int
    expenditure: float
    overclocking: float
    quantity_places: int
    volume_trunk: int
    car_id: Optional[int] = None