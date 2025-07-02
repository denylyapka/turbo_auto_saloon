from datetime import datetime

from typing import Optional
from app.models.dtoModels.Entity import Entity


class WatchListDTO(Entity):
    user_id: int
    car_id: Optional[int]
    detail_id: Optional[int]
