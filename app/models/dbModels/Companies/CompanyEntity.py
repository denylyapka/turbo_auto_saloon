# ARRAY для массивов (working_hours).
from sqlalchemy import Column, Integer, String, Text, ARRAY

from app.models.dbModels.base import Base


class CompanyEntity(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300))
    # Text для длинного текста без ограничения.
    short_description = Column(Text)
    description = Column(Text)
    # Массив строк, например, ["Пн-Пт: 9-18"].
    working_hours = Column(ARRAY(String))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
