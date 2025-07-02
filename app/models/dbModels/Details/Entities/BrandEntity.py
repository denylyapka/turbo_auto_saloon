from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, BigInteger, JSON, DateTime, Text
from sqlalchemy.orm import relationship


class Brand(EntityDB):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    logo_url = Column(String(255), nullable=True)
    
    detail = relationship("DetailEntity", back_populates="brand")

    def __init__(self, id=None, name=None, description=None, logo_url=None):
        self.id = id
        self.name = name
        self.description = description
        self.logo_url = logo_url
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "logo_url": self.logo_url
        }
