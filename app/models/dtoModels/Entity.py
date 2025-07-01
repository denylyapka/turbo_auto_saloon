from pydantic import BaseModel

class Entity(BaseModel):

    class Config:
        orm_mode = True
        from_attributes = True