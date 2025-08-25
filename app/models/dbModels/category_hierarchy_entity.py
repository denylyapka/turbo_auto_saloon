from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class CategoryHierarchyEntity(Base):
    __tablename__ = "category_hierarchies"
    id = Column(Integer, primary_key=True, index=True)
    parent_category = Column(Integer, ForeignKey("categories.id"))
    child_category = Column(Integer, ForeignKey("categories.id"))
