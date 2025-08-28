from sqlalchemy import Column, Integer, ForeignKey

from app.models.dbModels.base import Base


class CategoryHierarchyEntity(Base):
    __tablename__ = "category_hierarchies"

    id = Column(Integer, primary_key=True, index=True)
    parent_category = Column(Integer, ForeignKey("categories.id"))
    child_category = Column(Integer, ForeignKey("categories.id"))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
