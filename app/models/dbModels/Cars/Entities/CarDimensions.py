from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, Integer, SmallInteger
from sqlalchemy.orm import relationship


class CarDimensions(EntityDB):
    __tablename__ = 'car_dimensions'
    
    id = Column(Integer, primary_key=True)
    clearance = Column(SmallInteger, nullable=False)
    width = Column(SmallInteger, nullable=False)
    height = Column(SmallInteger, nullable=False)
    length = Column(SmallInteger, nullable=False)
    wheelbase = Column(SmallInteger, nullable=False)
    front_track = Column(SmallInteger, nullable=False)
    rear_track = Column(SmallInteger, nullable=False)
    
    # Relationship
    car = relationship("CarEntity", back_populates="dimensions", uselist=False)

    def __init__(self, id=None, clearance=None, width=None, height=None, length=None, wheelbase=None, front_track=None, rear_track=None):
        self.id = id
        self.clearance = clearance
        self.width = width
        self.height = height
        self.length = length
        self.wheelbase = wheelbase
        self.front_track = front_track
        self.rear_track = rear_track
    
    def to_dict(self):
        return {
            'id': self.id,
            'clearance': self.clearance,
            'width': self.width,
            'height': self.height,
            'length': self.length,
            'wheelbase': self.wheelbase,
            'front_track': self.front_track,
            'rear_track': self.rear_track
        }