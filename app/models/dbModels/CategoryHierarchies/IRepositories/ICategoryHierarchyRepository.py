from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.dtoModels.CategoryHierarchies.CategoryHierarchyDto import CategoryHierarchyCreate

from app.models.dbModels.CategoryHierarchies.Entities.CategoryHierarchyEntity import CategoryHierarchyEntity


class ICategoryHierarchyRepository(ABC):

    @abstractmethod
    def create(self, db: Session, ch: CategoryHierarchyCreate) -> CategoryHierarchyEntity:
        pass

    @abstractmethod
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[CategoryHierarchyEntity]:
        pass
