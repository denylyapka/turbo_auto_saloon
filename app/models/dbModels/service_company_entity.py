from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class ServiceCompanyEntity(Base):
    __tablename__ = "service_companies"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
