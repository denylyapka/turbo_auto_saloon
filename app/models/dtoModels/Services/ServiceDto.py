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
