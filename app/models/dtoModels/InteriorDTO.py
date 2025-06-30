from typing import Optional
from app.models.dtoModels.Entity import Entity


class InteriorDTO(Entity):
    id: int
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
    car_id: Optional[int] = None