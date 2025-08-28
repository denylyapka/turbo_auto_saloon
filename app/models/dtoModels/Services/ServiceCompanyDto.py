from pydantic import BaseModel


class ServiceCompanyBase(BaseModel):
    company_id: int
    service_id: int


class ServiceCompanyCreate(ServiceCompanyBase):
    pass


class ServiceCompany(ServiceCompanyBase):
    id: int

    class Config:
        from_attributes = True
