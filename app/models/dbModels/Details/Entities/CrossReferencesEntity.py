from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, Float, JSON, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


class CrossReference(EntityDB):
    __tablename__ = 'cross_references'
    
    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('details.id'), nullable=False)
    brand = Column(String(100), nullable=False)  # Бренд-аналог (например, "TRW")
    number = Column(String(100), nullable=False)  # Альтернативный артикул
    
    detail = relationship("DetailEntity", back_populates="cross_reference")

    def __init__(self, id=None, part_id=None, brand=None, number=None):
        self.id = id
        self.part_id = part_id
        self.brand = brand
        self.number = number
    
    def to_dict(self):
        return {
            'id': self.id,
            'part_id': self.part_id,
            'brand': self.brand,
            'number': self.number,
        }