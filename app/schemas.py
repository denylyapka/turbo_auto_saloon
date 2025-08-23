from pydantic import BaseModel
from typing import List


class ServiceBase(BaseModel):
    name: str
    short_description: str
    description: str
    price: float
    time_action: int
    photos: List[str]


class ServiceCreate(ServiceBase):
    pass


class Service(ServiceBase):
    id: int

    class Config:
        from_attributes = True


class CompanyBase(BaseModel):
    name: str
    short_description: str
    description: str
    working_hours: List[str]


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int

    class Config:
        from_attributes = True


class ServiceCompanyBase(BaseModel):
    company_id: int
    service_id: int


class ServiceCompanyCreate(ServiceCompanyBase):
    pass


class ServiceCompany(ServiceCompanyBase):
    id: int

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class CategoryHierarchyBase(BaseModel):
    parent_category: int
    child_category: int


class CategoryHierarchyCreate(CategoryHierarchyBase):
    pass


class CategoryHierarchy(CategoryHierarchyBase):
    id: int

    class Config:
        from_attributes = True
