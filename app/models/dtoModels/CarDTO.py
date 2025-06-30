from typing import List, Optional
from app.models.dtoModels.Entity import Entity

from app.models.dtoModels.EngineDTO import EngineDTO
from app.models.dtoModels.ChassisDTO import ChassisDTO
from app.models.dtoModels.DimensionsDTO import DimensionsDTO
from app.models.dtoModels.InteriorDTO import InteriorDTO


class CarDTO(Entity):
    id: int
    vin_id: str
    country_manufacturer: str
    description: str
    brand: str
    model: str
    year_of_release: int
    photos: List[str]
    mileage: int
    gear_box: str
    drive: str
    condition: str
    body_type: str
    color: str
    
    # Опциональные связи
    engine: Optional['EngineDTO'] = None
    chassis: Optional['ChassisDTO'] = None
    dimensions: Optional['DimensionsDTO'] = None
    interior: Optional['InteriorDTO'] = None