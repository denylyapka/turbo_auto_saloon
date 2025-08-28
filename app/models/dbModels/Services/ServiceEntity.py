from sqlalchemy import Column, Integer, String, Text, Float, ARRAY

from app.models.dbModels.base import Base


class ServiceEntity(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    short_description = Column(Text)
    description = Column(Text)
    price = Column(Float)  # Float для цен с десятичными.
    time_action = Column(Integer)
    photos = Column(ARRAY(String))  # Массив URL фото.

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
