from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.dtoModels.ServiceCompanies.ServiceCompanyDto import ServiceCompanyCreate

from app.models.dbModels.ServiceCompanies.Entities.ServiceCompanyEntity import ServiceCompanyEntity


class IServiceCompanyRepository(ABC):

    @abstractmethod
    def create(self, db: Session, sc: ServiceCompanyCreate) -> ServiceCompanyEntity:
        pass

    @abstractmethod
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[ServiceCompanyEntity]:
        pass
