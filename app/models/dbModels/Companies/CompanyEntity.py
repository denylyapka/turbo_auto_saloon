from sqlalchemy import Column, Integer, String, Text, ARRAY

from .Base import Base


class CompanyEntity(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300))
    short_description = Column(Text)
    description = Column(Text)
    working_hours = Column(ARRAY(String))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
