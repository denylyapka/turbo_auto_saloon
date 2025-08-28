from pydantic import BaseModel

from typing import List


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
