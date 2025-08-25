from sqlalchemy import Column, Integer, String
from .base import Base


class CategoryEntity(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(200))
