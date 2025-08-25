from sqlalchemy import Column, Integer, String, Text, Float, ARRAY
from .base import Base


class ServiceEntity(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    short_description = Column(Text)
    description = Column(Text)
    price = Column(Float)
    time_action = Column(Integer)
    photos = Column(ARRAY(String))
