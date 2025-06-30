from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict, Optional
from app.models.dtoModels.Entity import Entity


class EngineDTO(Entity):
    id: int
    turbine: bool
    engine_type: str  # gas, diesel, hybrid, electric
    engine_cylinders: int
    volume_engine: float
    power_hp: int
    power_nm: int
    car_id: Optional[int] = None