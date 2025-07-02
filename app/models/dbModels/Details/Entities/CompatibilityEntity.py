from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, Float, JSON, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


class Compatibility(EntityDB):
    __tablename__ = 'compatibilities'
    
    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('details.id'), nullable=False)
    make = Column(String(50), nullable=False)      # Марка (например, "Toyota")
    model = Column(String(50), nullable=False)     # Модель ("Camry")
    year_from = Column(Integer, nullable=True)     # Год начала
    year_to = Column(Integer, nullable=True)       # Год окончания
    engine_type = Column(String(50), nullable=True) # Тип двигателя ("2.5L бензин")
    
    detail = relationship("DetailEntity", back_populates="compatibility")

    def __init__(self, id=None, part_id=None, make=None, model=None, year_from=None, year_to=None, engine_type=None):
        self.id = id
        self.part_id = part_id
        self.make = make
        self.model = model
        self.year_from = year_from
        self.year_to = year_to
        self.engine_type = engine_type
    
    def to_dict(self):
        return {
            'id': self.id,
            'part_id': self.part_id,
            'make': self.make,
            'model': self.model,
            'year_from': self.year_from,
            'year_to': self.year_to,
            'engine_type': self.engine_type
        }