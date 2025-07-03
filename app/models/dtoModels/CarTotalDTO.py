from typing import List, Optional
from app.models.dtoModels.Entity import Entity


class CarTotalDTO(Entity):
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

    turbine: bool
    engine_type: str  # gas, diesel, hybrid, electric
    engine_cylinders: int
    volume_engine: float
    power_hp: int
    power_nm: int

    expenditure: float
    overclocking: float
    quantity_places: int
    volume_trunk: int

    clearance: int
    width: int
    height: int
    length: int
    wheelbase: int
    front_track: int
    rear_track: int

    conditioner: bool
    safety: Optional[str] = None
    steering_control_material: str
    steering_control_side: str
    steering_control_type_of_amplifier: str
    climate: Optional[str] = None
    wheel_diameter: int
    anti_theft: Optional[str] = None
    help_driving: Optional[str] = None
    salon_material: str
    salon_hatch: bool
    salon_color: str
    heated: Optional[str] = None
    electric: Optional[str] = None
    head_lights_type: str
    head_lights_washers: bool
    multumedia: Optional[str] = None
    quantity_speaker: int
    subwoofer: bool
    memory: Optional[str] = None


class CarFilterDTO(Entity):
    field: str
    value: str
    operator: str

class CarFiltersDTO(Entity):
    filters: list[CarFilterDTO]

