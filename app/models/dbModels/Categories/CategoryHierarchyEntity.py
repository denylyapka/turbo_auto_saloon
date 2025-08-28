# ForeignKey для связей между таблицами.
from sqlalchemy import Column, Integer, ForeignKey

from app.models.dbModels.base import Base

# Модель для иерархии категорий (82.5).


class CategoryHierarchyEntity(Base):
    __tablename__ = "category_hierarchies"

    id = Column(Integer, primary_key=True, index=True)
    # Ссылка на родительскую категорию (FK — foreign key).
    parent_category = Column(Integer, ForeignKey("categories.id"))
    # Ссылка на дочернюю категорию.
    child_category = Column(Integer, ForeignKey("categories.id"))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
