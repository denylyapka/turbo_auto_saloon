from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Category(EntityDB):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    
    detail = relationship("DetailEntity", back_populates="category")

    def __init__(self, id=None, name=None, parent_id=None):
        self.id = id
        self.name = name
        self.parent_id = parent_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent_id': self.parent_id
        }