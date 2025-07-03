from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, BigInteger, JSON, DateTime, Text, ARRAY, Boolean, Float, SmallInteger
from sqlalchemy.orm import relationship


class CarEngine(EntityDB):
    __tablename__ = 'car_engines'
    
    id = Column(Integer, primary_key=True)
    turbine = Column(Boolean, nullable=True)
    engine_type = Column(String, nullable=True)  # gas, diesel, hybrid, electric
    engine_cylinders = Column(SmallInteger, nullable=True)
    volume_engine = Column(Float, nullable=True)
    power_hp = Column(Integer, nullable=True)
    power_nm = Column(Integer, nullable=True)
    
    # Relationship
    car = relationship("CarEntity", back_populates="engine", uselist=False)

    def __init__(
        self, id=None, turbine=None, engine_type=None, engine_cylinders=None, volume_engine=None, power_hp=None, power_nm=None
    ):
        self.id = id
        self.turbine = turbine
        self.engine_type = engine_type
        self.engine_cylinders = engine_cylinders
        self.volume_engine = volume_engine
        self.power_hp = power_hp
        self.power_nm = power_nm
    
    def to_dict(self):
        return {
            'id': self.id,
            'turbine': self.turbine,
            'engine_type': self.engine_type,
            'engine_cylinders': self.engine_cylinders,
            'volume_engine': self.volume_engine,
            'power_hp': self.power_hp,
            'power_nm': self.power_nm
        }
