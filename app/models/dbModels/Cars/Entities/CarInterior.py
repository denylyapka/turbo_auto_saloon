from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, Boolean, SmallInteger
from sqlalchemy.orm import relationship


class CarInterior(EntityDB):
    __tablename__ = 'car_interiors'
    
    id = Column(Integer, primary_key=True)
    conditioner = Column(Boolean, nullable=True)
    safety = Column(String, nullable=True)
    steering_control_material = Column(String(50), nullable=True)
    steering_control_side = Column(String(50), nullable=True)
    steering_control_type_of_amplifier = Column(String(50), nullable=True)
    climate = Column(String, nullable=True)
    wheel_diameter = Column(SmallInteger, nullable=True)
    anti_theft = Column(String, nullable=True)
    help_driving = Column(String, nullable=True)
    salon_material = Column(String(200), nullable=True)
    salon_hatch = Column(Boolean, nullable=True)
    salon_color = Column(String(200), nullable=True)
    heated = Column(String, nullable=True)
    electric = Column(String, nullable=True)
    head_lights_type = Column(String(50), nullable=True)
    head_lights_washers = Column(Boolean, nullable=True)
    multumedia = Column(String, nullable=True)
    quantity_speaker = Column(SmallInteger, nullable=True)
    subwoofer = Column(Boolean, nullable=True)
    memory = Column(String, nullable=True)
    
    # Relationship
    car = relationship("CarEntity", back_populates="interior", uselist=False)

    def __init__(
        self, id=None, conditioner=None, safety=None, steering_control_material=None, steering_control_side=None,
        steering_control_type_of_amplifier=None, climate=None, wheel_diameter=None, anti_theft=None, help_driving=None,
        salon_material=None, salon_hatch=None, salon_color=None, heated=None, electric=None, head_lights_type=None,
        head_lights_washers=None, multumedia=None, quantity_speaker=None, subwoofer=None, memory=None
    ):
        self.id = id
        self.conditioner = conditioner
        self.safety = safety
        self.steering_control_material = steering_control_material
        self.steering_control_side = steering_control_side
        self.steering_control_type_of_amplifier = steering_control_type_of_amplifier
        self.climate = climate
        self.wheel_diameter = wheel_diameter
        self.anti_theft = anti_theft
        self.help_driving = help_driving
        self.salon_material = salon_material
        self.salon_hatch = salon_hatch
        self.salon_color = salon_color
        self.heated = heated
        self.electric = electric
        self.head_lights_type = head_lights_type
        self.head_lights_washers = head_lights_washers
        self.multumedia = multumedia        
        self.quantity_speaker = quantity_speaker
        self.subwoofer = subwoofer
        self.memory = memory
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}