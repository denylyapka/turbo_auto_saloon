from sqlalchemy import Column, Integer, String, Text, ARRAY
from .base import Base


class CompanyEntity(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300))
    short_description = Column(Text)
    description = Column(Text)
    working_hours = Column(ARRAY(String))
