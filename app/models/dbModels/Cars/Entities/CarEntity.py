from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, Text, ARRAY, ForeignKey
from sqlalchemy.orm import relationship


class CarEntity(EntityDB):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True, nullable=False)
    vin_id = Column(String(100), nullable=False)
    country_manufacturer = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    brand = Column(String(100), nullable=False)
    model = Column(String(200), nullable=False)
    year_of_release = Column(Integer, nullable=False)
    photos = Column(ARRAY(String), nullable=False)
    mileage = Column(Integer, nullable=False)
    gear_box = Column(String(50), nullable=False)
    drive = Column(String(50), nullable=False)
    condition = Column(String(50), nullable=False)
    body_type = Column(String(50), nullable=False)
    color = Column(String(100), nullable=False)
    
    # Связи с другими таблицами
    engine_id = Column(Integer, ForeignKey('car_engines.id'))
    chassis_id = Column(Integer, ForeignKey('car_chassis.id'))
    dimensions_id = Column(Integer, ForeignKey('car_dimensions.id'))
    interior_id = Column(Integer, ForeignKey('car_interiors.id'))
    
    # Relationships
    engine = relationship("CarEngine", back_populates="car")
    chassis = relationship("CarChassis", back_populates="car")
    dimensions = relationship("CarDimensions", back_populates="car")
    interior = relationship("CarInterior", back_populates="car")

    def __init__(
            self, id=None, vin_id=None, country_manufacturer=None, description=None, brand=None,
            model=None, year_of_release=None, photos=None, mileage=None, gear_box=None, drive=None,
            condition=None, body_type=None, color=None
        ):
        self.id = id
        self.vin_id = vin_id
        self.country_manufacturer = country_manufacturer
        self.description = description
        self.brand = brand
        self.model = model
        self.year_of_release = year_of_release
        self.photos = photos
        self.mileage = mileage
        self.gear_box = gear_box
        self.drive = drive
        self.condition = condition
        self.body_type = body_type
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "vin_id": self.vin_id,
            "country_manufacturer": self.country_manufacturer,
            "description": self.description,
            "brand": self.brand,
            "model": self.model,
            "year_of_release": self.year_of_release,
            "photos": self.photos,
            "mileage": self.mileage,
            "gear_box": self.gear_box,
            "drive": self.drive,
            "condition": self.condition,
            "body_type": self.body_type,
            "color": self.color
        }