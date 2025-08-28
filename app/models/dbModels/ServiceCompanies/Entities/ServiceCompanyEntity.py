from sqlalchemy import Column, Integer, ForeignKey

from app.models.dbModels.base import Base


class ServiceCompanyEntity(Base):
    __tablename__ = "service_companies"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    service_id = Column(Integer, ForeignKey("services.id"))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
