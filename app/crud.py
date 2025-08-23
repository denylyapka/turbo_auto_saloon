from sqlalchemy.orm import Session
from . import models, schemas


def create_service(db: Session, service: schemas.ServiceCreate):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()


def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()


def create_service_company(db: Session, sc: schemas.ServiceCompanyCreate):
    db_sc = models.ServiceCompany(**sc.dict())
    db.add(db_sc)
    db.commit()
    db.refresh(db_sc)
    return db_sc


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category_hierarchy(db: Session, ch: schemas.CategoryHierarchyCreate):
    db_ch = models.CategoryHierarchy(**ch.dict())
    db.add(db_ch)
    db.commit()
    db.refresh(db_ch)
    return db_ch
