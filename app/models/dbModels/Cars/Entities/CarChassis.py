from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, Integer, Float, SmallInteger
from sqlalchemy.orm import relationship


class CarChassis(EntityDB):
    __tablename__ = 'car_chassis'

    id = Column(Integer, primary_key=True)
    expenditure = Column(Float, nullable=True)
    overclocking = Column(Float, nullable=True)
    quantity_places = Column(SmallInteger, nullable=True)
    volume_trunk = Column(SmallInteger, nullable=True)
    
    # Relationship
    car = relationship("CarEntity", back_populates="chassis", uselist=False)

    def __init__(self, id=None, expenditure=None, overclocking=None, quantity_places=None, volume_trunk=None):
        self.id = id
        self.expenditure = expenditure
        self.overclocking = overclocking
        self.quantity_places = quantity_places
        self.volume_trunk = volume_trunk

    def to_dict(self):
        return {
            'id': self.id,
            'expenditure': self.expenditure,
            'overclocking': self.overclocking,
            'quantity_places': self.quantity_places,
            'volume_trunk': self.volume_trunk
        }
